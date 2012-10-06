import web
import MySQLdb as db
import controller

render = web.template.render('app/src/views/')


urls = (
    '/', 'index',
    '/add', 'add',
    '/route', 'one',
    '/hello', 'hello',
    '/hello/control', 'hello_control'
)

app = web.application(urls, globals())

class index: 
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

class one:
    def POST(self, route_number):
        i = web.input()
        n = db.insert('todo', title=i.title)
        return render.route_1_sonar(route_number)

class hello:
    def GET(self):
        return render.hello()

class hello_control:
    def GET(self):
        return render.hello_control()


class users:
    def GET(self, user):
        return render.users(user)

#create table todo ( id int not null primary key auto_increment, title varchar(100), created timestamp default now(), done boolean not null default 0  );
db = web.database(dbn='mysql', user='busbeep', pw='DannyBoy6812', db='busbeep_dev')

def run():
    return app.run()

if __name__ == "__main__":
    run()

