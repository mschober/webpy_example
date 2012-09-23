import web

urls = (
    '/hello', 'hello'
)

app = web.application(urls, globals())
render = web.template.render('app/src/resources')

class hello():
    def GET(self):
        return render.hello()
