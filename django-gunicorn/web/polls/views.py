from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
def index(request):
    # Example: Theme using "render" shortcut.
    latest_question_list = Question.objects.order_by('-pub_date')[:4]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

    # Example: Theme using template and HttpResponse.#
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # Example: Theme directly in view.
    # output = "<br />".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


def detail(request, question_id):
    # Example: Use Django shortcut to raise a 404 if object does not exist
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        'question': question
    })

    # Example: Verbose method to raise a 404 exception
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return render(request, 'polls/detail.html', {
    #     'question': question
    # })

    # Example: Don't raise Exception when object does not exist.
    # question = Question.objects.get(pk=question_id)
    # return render(request, 'polls/detail.html', {
    #     'question': question
    # })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })


def vote(request, question_id):
    # Determine if the path is a "view" path.
    url_parts = request.path.strip('/').split('/')
    is_view = ('view' in url_parts)
    if (is_view):
        url_error = 'polls/views/detail.html'
        url_redirect = 'polls:view_results'
    else:
        url_error = 'polls/detail.html'
        url_redirect = 'polls:results'

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, url_error, {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if
        # a user hits the "back" button.
        return HttpResponseRedirect(reverse(url_redirect, args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls_views/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published question."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls_views/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls_views/results.html'

