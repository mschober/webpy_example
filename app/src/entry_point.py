import web
import controllers

render = web.template.render('app/src/views')

urls = (
    '/hello', 'hello',
    '/route', 'controllers.route.index'
)

app = web.application(urls, globals())

class hello:
    def GET(self):
        return render.hello()

if __name__ == "__main__":
    app.run()

