from django.contrib import messages
from django.shortcuts import redirect, render

from models import *
def noname(req):
    return 'id' not in req.session

def index(req):
    req.session.clear()
    return render(req, "regis/index.html")

def login(req):
    result = User.manager.login(req.POST)
    if result[0]:
        req.session['id'] = result[1].id
        user = User.manager.get(id=req.session['id'])
        Messages.objects.create(message = "" + user.user_name + " has just logged in.", user = None)
        return redirect('/success')
    for key, message in result[1].iteritems():
        messages.error(req,message)
    return redirect('/')

def register(req):
    result = User.manager.createUser(req.POST)
    if result[0]:
        req.session['id'] = result[1].id
        user = User.manager.get(id=req.session['id'])
        Messages.objects.create(message = "" + user.user_name + " has just made a account, welcome them.", user = None)
        return redirect('/success')
    
    for key, message in result[1]:
        messages.error(req, message)
    return redirect('/')

def message(req):
    result = Messages.manager.createMessages(req.POST)
    if len(result):
        for tag, error in result.iteritems():
            messages.error(req, error, extra_tags=tag)
        message = Messages.objects.all()
        return render(req, 'regis/all.html', {'messages': message})
    else:
        user = User.manager.get(id=req.session['id'])
        Messages.objects.create(message = req.POST['message'], user = user)
        message = Messages.objects.all()
        return render(req, 'regis/all.html', {'messages': message})

def success(req):
    if noname(req):
        return redirect('/')
    user = User.manager.get(id=req.session['id'])
    message = Messages.objects.all()
    context = {
        'self': user,
        'messages': message
    }
    return render(req, "regis/success.html", context)


def logout(req):
    user = User.manager.get(id=req.session['id'])
    Messages.objects.create(message = "" + user.user_name + " Has logged out", user = None)
    req.session.clear()
    return redirect('/')

def load(req):
    message = Messages.objects.all()
    return render(req, 'regis/all.html', {'messages': message})