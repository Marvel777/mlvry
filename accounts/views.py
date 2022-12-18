from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
import speech_recognition as sr
from products.models import Product#Chat
import re
# Create your views here.

def signin(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:
        
        username = request.POST['user']
        password = request.POST['pass']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            messages.success(request, 'You are logged in')
        else:
            messages.error(request, 'Username or password invalid')
            
        return redirect('signin')
    else: 
        return render( request , 'accounts/signin.html' )

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        #variable for fields
        fname =None
        lname = None
        address = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        #get values from the form
        if 'fname' in request.POST: fname = request.POST['fname']
        else: messages.error(request, 'Error in first name')
        if 'lname' in request.POST: lname = request.POST['lname']
        else: messages.error(request, 'Error in last name')
        if 'address' in request.POST: address = request.POST['address']
        else: messages.error(request, 'Error in address')
        if 'city' in request.POST: city = request.POST['city']
        else: messages.error(request, 'Error in city')
        if 'state' in request.POST: state = request.POST['state']
        else: messages.error(request, 'Error in state')
        if 'zip' in request.POST: zip_number = request.POST['zip']
        else: messages.error(request, 'Error in zip')
        if 'email' in request.POST: email=request.POST['email']
        else: messages.error(request, 'Error in email')
        if 'user' in request.POST: username = request.POST['user']
        else: messages.error(request, 'Error in user')
        if 'pass' in request.POST: password = request.POST['pass']
        else: messages.error(request, 'Error in password')
        if 'terms' in request.POST: terms = request.POST['terms']
        
        #check values
        if fname and lname and address and city and state and zip_number and email and username and password:
            if terms == 'on':
                #check if username is taken
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'This username is taken')
                else:
                    #check if email is taken
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'This email is taken')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt, email):
                            #add user
                            user =  User.objects.create_user(first_name=fname,last_name=lname, email=email, username=username, password=password)
                            user.save()
                            #add user profil
                            userprofile = UserProfile(user=user, address=address,city=city, state=state, zip_number=zip_number)
                            userprofile.save()
                            #clear fields
                            fname = ''
                            lname = ''
                            address = ''
                            city = ''
                            state = ''
                            zip_number =''
                            email = ''
                            username = ''
                            password = ''
                            terms = None
                            #success messge
                            messages.success(request,'Your account is created')
                            
                        else:
                            messages.error(request, 'Invaild email')
            else:
                messages.error(request, 'You must agree to the terms')
        else:
            messages.error(request, 'Check empty fields')
            
        
        return render( request ,'accounts/signup.html',{
            'fname':fname,
            'lname':lname,
            'address':address,
            'city':city,
            'state':state,
            'zip':zip_number,
            'email':email,
            'user':username,
            'pass':password,
        })
    else: 
        return render( request ,'accounts/signup.html')

def product_favorite(request , pro_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        pro_fav = Product.objects.get(pk=pro_id)
        if UserProfile.objects.filter(user=request.user,product_favorites=pro_fav).exists():
            messages.success(request,'Already product in the favorite list ')
        else:
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.product_favorites.add(pro_fav)
            messages.success(request,'Product has been favorited')
    else:
        messages.error(request,'You must be logged in')
    return redirect('/products/' + str(pro_id))


def show_product_favorite(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = UserProfile.objects.get(user=request.user)
        pro = userInfo.product_favorites.all()
        context = {'products':pro}
    return render(request, 'products/products.html', context)