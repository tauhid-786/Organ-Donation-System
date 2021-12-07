from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from .models import *
# Create your views here.

def Home(request):
    print('you are',request.session.get('donar'))
    return render(request, "home.html", context=None)

def Cornea(request):
    return render(request, "cornea.html", context=None)

def Heart(request):
    return render(request, "heart.html", context=None)

def Intestine(request):
    return render(request, "intestine.html", context=None)

def Kidney(request):
    return render(request, "kidney.html", context=None)

def Liver(request):
    return render(request, "liver.html", context=None)

def Lungs(request):
    return render(request, "lungs.html", context=None)

def Pancrease(request):
    return render(request, "pancrease.html", context=None)

def Tissue(request):
    return render(request, "tissue.html", context=None)


class Signup(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        donar = Donar(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateDonar(donar)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            donar.password = make_password(donar.password)
            donar.register()
            return redirect('/')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'register.html', data)

    def validateDonar(self, donar):
        error_message = None;
        if (not donar.first_name):
            error_message = "First Name Required !!"
        elif len(donar.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not donar.last_name:
            error_message = 'Last Name Required'
        elif len(donar.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not donar.phone:
            error_message = 'Phone Number required'
        elif len(donar.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(donar.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(donar.email) < 5:
            error_message = 'Email must be 5 char long'
        elif donar.isExist():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


class Login(View):
    def get(self , request):
        return render(request , 'login.html')
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        donar = Donar.get_donar_by_email(email)
        error_message = None
        if donar:
            flag = check_password(password, donar.password)
            if flag:
                request.session['donar'] = donar.id
                request.session['email'] = donar.email
                request.session['name'] = donar.first_name
                return redirect('/')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

class Donate(View):
    def get(self , request):
        return render(request , 'donate.html')
    def post(self , request):
        organ_name = request.POST.get('organ_name')
        quantity = request.POST.get('quantity')
        hospital_name = Donar.get_donar_by_email('hospital_name')
        hospital_address = request.POST.get('hospital_address')
        hospital_phone = request.POST.get('hospital_phone')
        inst=Organ(
            organ_name=organ_name,
            quantity=quantity,
            hospital_name =hospital_name,
            hospital_address=hospital_address,
            hospital_phone =hospital_phone,
        )
        inst.save()
        return redirect('/')


        error_message = None
        if donar:
            flag = check_password(password, donar.password)
            if flag:
                request.session['donar'] = donar.id
                request.session['email'] = donar.email
                request.session['name'] = donar.first_name
                return redirect('/')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})
def Logout(request):
        request.session.clear()
        return redirect('/login')

class Available(View):
    def get(self , request):
        org = Organ.objects.all()
        return render(request , 'available.html',{"key":org})
    
# class OrderView(View):
#     def get(self , request ):
#         customer = request.session.get('customer')
#         orders = Order.get_orders_by_customer(customer)
#         print(orders)
#         return render(request , 'orders.html'  , {'orders' : orders})