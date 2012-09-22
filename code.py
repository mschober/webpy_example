import web
import MySQLdb as db

render = web.template.render('templates/')

urls = (
    #'/users/(.*)', 'users',
    #'/(.*)', 'index'
    '/', 'index',
    '/add', 'add'
)


class index: 
    #def GET(self, name):
    #    return render.index(name)
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

class users:
    def GET(self, user):
        return render.users(user)

#create table todo ( id int not null primary key auto_increment, title varchar(100), created timestamp default now(), done boolean not null default 0  );
db = web.database(dbn='mysql', user='busbeep', pw='DannyBoy6812', db='busbeep_dev')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
