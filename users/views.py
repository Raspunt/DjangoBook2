from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
