#!/usr/bin/env python

# Run this with
# export PYTHONPATH=.; export DJANGO_SETTINGS_MODULE=django_and_rethinkdb.settings; python django_and_rethinkdb/tornado_main.py

import django.core.handlers.wsgi
from django.conf import settings
import os
from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.websocket
import tornado.gen
from change_feed import print_changes, SocketHandler, MessageHandler

django.setup()

def main():
  parse_command_line()
  wsgi_app = tornado.wsgi.WSGIContainer(
    django.core.handlers.wsgi.WSGIHandler()
  )
  current_dir = os.path.dirname(os.path.abspath(__file__))
  static_folder = os.path.join(current_dir, 'static')
  tornado_app = tornado.web.Application([
    ('/new-messages/', SocketHandler),
    ('/messages/', MessageHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, { 'path': static_folder }),
    ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
  ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(8000)
  tornado.ioloop.IOLoop.current().add_callback(print_changes)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
