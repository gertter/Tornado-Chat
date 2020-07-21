import tornado
from tornado import web

from config.settings import settings
from routers.Routes import patterns


def main():
    app = web.Application(patterns, **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
if __name__=="__main__":
    main()
