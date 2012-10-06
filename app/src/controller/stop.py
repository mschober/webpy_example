import web

render = web.template.render('app/src/views')

class index:
    def GET(self, the_route, the_bus):
        return render.stop(the_route)

class show:
    def GET(self, the_route, the_bus, the_stop):
        return render.specific_stop(the_route, the_bus, the_stop)
