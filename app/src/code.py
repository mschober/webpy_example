import web
import MySQLdb as db

render = web.template.render('app/src/resources/')

import web
import src.controllers

urls = (
    #'/submit_application',                       'src.controllers.submit_application.apply',
    #'/submit_reference/([0-9a-f]{32})',          'src.controllers.submit_reference.refer',
    #'/affiliated/submit_application',            'src.controllers.submit_application.apply_simple',
    #
    #'/(|new|pending|all|admitted)',              'src.controllers.browse.list',
    #'/(search|rejected|reviewed)',               'src.controllers.browse.list',
    #'/applicant/(\d+)',                          'src.controllers.browse.show',
    #
    #'/admit',                                    'src.controllers.actions.admit',
    #'/reject',                                   'src.controllers.actions.reject',
    #'/undecide',                                 'src.controllers.actions.undecide',
    #'/rate',                                     'src.controllers.actions.rate',
    #
    #'/applicant/(\d+)/comment',                  'src.controllers.actions.comment',
    #'/delete_comment/(\d+)',                     'src.controllers.actions.delete_comment',
    #
    #'/grant/(\d+)',                              'src.controllers.actions.grant',
    
    '/route',                                  'src.controllers.route.index'
    #'/route/register',                         'src.controllers.route.register',
    #'/route/login',                            'src.controllers.route.login',
    #'/route/logout',                           'src.controllers.route.logout',
    #'/route/resend_password',                  'src.controllers.route.resend_password',
    #'/route/help',                             'src.controllers.route.help'
    
    #'/settings',                                 'src.controllers.settings.index',
    #'/settings/change_nickname',                 'src.controllers.settings.change_nickname',
    #'/settings/change_password',                 'src.controllers.settings.change_password',
    #'/settings/change_email',                    'src.controllers.settings.change_email',
    #
    #'/(?:img|js|css)/.*',                        'src.controllers.public.public',

    #'/tests/session',                            'src.tests.session',
    #'/tests/upload',                             'src.tests.upload',
)
urls = (
    #'/users/(.*)', 'users',
    #'/(.*)', 'index'
    '/', 'index',
    '/add', 'add',
    '/route', 'one',
    '/hello', 'hello',
    '/hello/control', 'hello_control'
)

app = web.application(urls, globals())

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

if __name__ == "__main__":
    app.run()
