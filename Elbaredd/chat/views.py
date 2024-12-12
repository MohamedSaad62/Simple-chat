from django.shortcuts import render
from .models import User_name, messages
def login(request):
        return render(request, 'login.html')


def create(request):
        return render(request, 'create.html')


def loging(request):
        user_name = request.POST['username'];
        cnt = User_name.objects.filter(user_text = user_name).count()
        if cnt == 1:
                dic = {'user' : user_name, 'users' : User_name.objects.all()}
                return render(request, 'loging.html', dic)
        else:
                return render(request, 'loging_error.html', {'user' : user_name})        



def creating(request):
        user_name = request.POST['username'];
        cnt = User_name.objects.filter(user_text = user_name).count()
        if cnt == 0:
                User_name(user_text = user_name).save()
                return render(request, 'creating.html', {'user' : user_name})

        else :
               return render(request, 'f_creating.html', {'user' : user_name})         


def chatRoom(request):
        sender = request.POST['sender']
        reciever = request.POST['reciever']
        s = ''
        if sender > reciever:
                s += sender
                s += reciever
        else :
                s += reciever
                s += sender   
        c = messages.objects.filter(identifier = s).count()
        msgs = 'No messages yet'
        if c > 0 :
                msgs = messages.objects.filter(identifier = s)        
        dic = {'sender' : sender, 'reciever' : reciever, 'msgs' : msgs, 'c' : c}
        return render(request, 'chatRoom.html', dic)


def newMessage(request):
        sender = request.POST['sender']
        reciever = request.POST['reciever']
        msg = request.POST['msg']
        s = ''
        if sender > reciever:
                s += sender
                s += reciever
        else :
                s += reciever
                s += sender        
        messages(sender = sender, reciever = reciever, message = msg, identifier = s).save()
        return chatRoom(request)