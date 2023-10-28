from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
import inflect

# Create your views here.
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"successful login")
            return redirect('home')
        else:
            messages.success(request,"failed to login")
            return redirect('home')
    else:
        return render(request,'home.html')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"you were logged out")
    return redirect('home')

def quote_form_v1(request):
    return render(request,'quote_form_v1.html',{})

def los(request):
    selected_option = request.POST.get('option')
    print(type(selected_option))
    opt_integer = int(selected_option)
    items_to_display = range(opt_integer)
    context={
        'items_to_display':items_to_display,
    }
    return render(request,'quote_form_v1.html',context=context)

def quote(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%d/%m/%Y")
        a1=request.POST.get('a1')
        a2=request.POST.get('a2')
        a3=request.POST.get('a3')
        nof=request.POST.get('nof')
        nof_int = int(nof)
        nof_int = range(nof_int)
        desclist=[]
        hsnlist=[]
        qtylist=[]
        unitlist=[]
        ratelist=[]
        amountlist=[]
        for i in range(len(nof_int)):
            desclist.append(request.POST.get(f'desc{i}'))
            hsnlist.append(request.POST.get(f'hsn{i}'))
            qtylist.append(request.POST.get(f'qty{i}'))
            unitlist.append(request.POST.get(f'unit{i}'))
            ratelist.append(request.POST.get(f'rate{i}'))
            amountlist.append(request.POST.get(f'amount{i}'))
        int_amountlist=[int(x) if x.isdigit() else 0 for x in amountlist]
        sumlist=sum(int_amountlist)
        p = inflect.engine()
        text= p.number_to_words(sumlist)
        text=text.upper()  
        combined_data = []
        for a, b, c, d, e, f in zip(desclist, hsnlist, qtylist, unitlist, ratelist,int_amountlist):
            combined_data.append({'a': a, 'b': b, 'c': c, 'd': d, 'e': e,'f':f,})

        context={
            'd':date,'a1':a1,'a2':a2,'a3':a3,'nof':nof,'t':text,'sum':sumlist,'combined_data':combined_data,
        }
        return render(request,'preview.html',context=context)