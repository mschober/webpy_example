import web

render = web.template.render('app/src/view')

class index:
    def GET(self, theRoute):
        return render.bus(theRoute)

class show:
    def GET(self, theRoute, theBus):
        return render.specific_bus(theBus)
