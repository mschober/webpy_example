import web

render = web.template.render('app/src/views')

class index:
    def GET(self, the_route, the_bus):
        return render.stop(the_route)
