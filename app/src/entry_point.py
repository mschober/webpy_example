import web
import controllers
import os

render = web.template.render('app/src/views')

urls = (
    '/hello',                           'hello',
    '/route',                           'controllers.route.index',
    '/route/(\d+)',                     'controllers.route.show',
    '/route/(\d+)/bus',                 'controllers.bus.index',
    '/route/(\d+)/bus/(\d+)',           'controllers.bus.show',
    '/route/(\d+)/bus/(\d+)/stop',      'controllers.stop.index',
)

app = web.application(urls, globals())

class hello:
    def GET(self):
        return render.hello()

def is_test():
    if 'WEBPY_ENV' in os.environ:
        return os.environ['WEBPY_ENV'] == 'test'

if (not is_test()) and __name__ == "__main__": app.run()

