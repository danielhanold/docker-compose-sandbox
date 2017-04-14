from django.http import HttpResponse


def project_custom_404_page(request):
    """
    Custom handler for 404 page.
    """
    return HttpResponse('Yet another way to do a custom 404 page. This overwrites the default location in /templates/404.html.')