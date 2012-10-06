import web


render = web.template.render('app/src/view/')

class index:
    def GET(self):
        return render.route()

class show:
    def GET(self, theRoute):
        return render.show_route(theRoute)
