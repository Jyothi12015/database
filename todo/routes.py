from flask import request,render_template,jsonify,make_response
from .utils import saferequest
from todo.models import Session,Todo,User
import uuid  
from todo.db import where

def configure_bot_routes(app):
    @app.route('/')
    @saferequest()
    def greet(*args, **kwargs):
        from .data.about import bot #controller
        name = None
        if kwargs.get('session',None):
            name=kwargs['session'].name

        return render_template('index.html',title='Home',data=bot,name=name)
    
    @app.route('/summary')
    @saferequest()
    def summary(*args,**kwargs):
        from .data.summary import make_summary
        d=make_summary()
        return jsonify(d)

    @app.route('/auth',methods = ['POST'])
    @saferequest(None,401)
    def auth(*args,**kwargs):
        if request.form['mode']:
            mode=request.form['mode']
            username = request.form['username']
            password = request.form['password']
            name=request.form.get('name',None)
            if mode == 'login': 
                user=User.validate(username,password)
            else:
                userid = User.register(name,username,password)
                user=User.retrieve(userid)
            #create a new session
            if kwargs.get('session',None):
                Session.delete(where('sessionid')==kwargs.get('session').sessionid)

            sessionid=str(uuid.uuid4())
            Session.create(sessionid=sessionid,userid=user.id,name=user.name)

            resp = make_response(render_template('messages/greet.html',name=user.name,key="request"))
            resp.set_cookie('sessionid',sessionid)
            return resp
        else:
            return ''

    @app.route('/message',methods=['POST'])
    @saferequest
    def message(*args,**kwargs):
        if request.method == 'POST':
            message=request.form['message']
            from .intents import handle
            kwargs.update(request.form)
            return handle(*args,**kwargs)
        else:
            return ''

    @app.route('/addtodo',methods=['POST'])
    @saferequest
    def addtodo(*args,**kwargs):
        if 'session' not in kwargs:
            return "Login required",401

        if request.method == 'POST':
            userid=kwargs['session'].userid
            task = request.form['task']
            due = request.form['due']
            created = request.form['created']
            priority=int(request.form['priority'])

            Todo.create(userid=userid,task=task,due=due,priority=priority)
            return render_template('message/newtask.html')
        else:
            return ''