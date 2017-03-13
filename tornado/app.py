#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.escape
import tornado.web
import os.path
import json
from elasticsearch import Elasticsearch

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
             (r"/", HomeHandler),
             (r"/story/([^/]+)", StoryHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            site_title=u'DnaInfo - Python POC',
            dna_host=u'http://www.dnainfo.com',
            debug=False,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"
        )
        super(Application, self).__init__(handlers, **settings)
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("user_token")

class HomeHandler(BaseHandler):
    def get(self):
        self.render("home.html")

    def post(self):
        searchTerm = self.get_argument("keyword")
        es = Elasticsearch([{'host':'elasticsearch', 'port':9200}])

        results = es.search(index='index', q=searchTerm, sort="created:desc")['hits']['hits']
        self.render("home.html", results=results)

class StoryHandler(BaseHandler):
    def get(self, story):
        searchTerm = story
        es = Elasticsearch([{'host':'elasticsearch', 'port':9200}])

        result = es.search(index='index', q=searchTerm, sort="created:desc")['hits']['hits']
        self.render("story.html", result=result)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
