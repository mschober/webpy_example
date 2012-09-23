import web


render = web.template.render('app/src/views/')

class index:
    def GET(self):
        return render.route()
