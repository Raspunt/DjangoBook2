from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.core.exceptions import ObjectDoesNotExist
from colorama import Fore, Back, Style
from . models import *

def register(request):
    errorMessage = ''

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName  = request.POST.get('LastName')
        email     = request.POST.get('email')
        userName  = request.POST.get('UserName')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2 :
            errorMessage = "Пароли не совпадают"
        else :

            newUser = User(first_name = firstName,
                            last_name = lastName,
                            email = email,
                            username = userName)

            newUser.set_password(password1)
            newUser.save()

            return redirect('/')




    return render(request,'users/register.html',{'Wrong_Password':errorMessage})




def userProfileTempate(request):

    name = request.POST.get('name')
    img  = request.FILES.get('img')
    desc = request.POST.get('desc')

    



    if request.user.is_authenticated != True:
        return redirect('/login')

    user = User.objects.get(username=request.user)
    try :

        userprof = UserProfile.objects.get(name=user) # если нет в базе вызывает ObjectDoesNotExist
        
        if request.method == "POST":

            if name != str(request.user):
                user.username = name
                user.save()
                print("изменено имя в бд")
            if img != '' and img != None:
                userprof.img = img
            if desc != '' and desc != None:
                userprof.desc = desc 

            userprof.save()
                
                



        data = {
            'user':user,
            'userPr':userprof
        }
        return render(request,"users/userDetail.html",data)
        



    except ObjectDoesNotExist as e:
        print(Fore.RED +"Нету профиля  ObjectDoesNotExist")
        data = {}

        if request.method == "POST":
            

            
            newuserprof = UserProfile.objects.create(name=user,desc=desc,img=img,rating=100.0)

            newuserprof.name = user
            newuserprof.desc = desc
            newuserprof.img = img
            newuserprof.rating = 100.0


            data['userPr'] = newuserprof
        
        data['user'] = user
        


 
        return render(request,"users/userDetail.html",data)
