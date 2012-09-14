import web
render = web.template.render('templates/')

urls = (
    '/users/(.*)', 'users',
    '/(.*)', 'index'
)


class index: 
    def GET(self, name):
        return render.index(name)

class users:
    def GET(self, user):
        return render.users(user)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
