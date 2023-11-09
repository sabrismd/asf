from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
import inflect
import locale

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
def quote_form_v2(request):
    return render(request,'quote_form_v2.html',{})
def bill_form(request):
    return render(request,'bill_form_v1.html',{})
def bill_form2(request):
    return render(request,'bill_form_v2.html',{})

def los(request):
    selected_option = request.POST.get('option')
    print(type(selected_option))
    opt_integer = int(selected_option)
    items_to_display = range(opt_integer)
    context={
        'items_to_display':items_to_display,
    }
    return render(request,'quote_form_v1.html',context=context)

def los2(request):
    selected_option = request.POST.get('option')
    print(type(selected_option))
    opt_integer = int(selected_option)
    items_to_display = range(opt_integer)
    context={
        'items_to_display':items_to_display,
    }
    return render(request,'quote_form_v2.html',context=context)
def los3(request):
    selected_option = request.POST.get('option')
    print(type(selected_option))
    opt_integer = int(selected_option)
    items_to_display = range(opt_integer)
    context={
        'items_to_display':items_to_display,
    }
    return render(request,'bill_form_v1.html',context=context)
def los4(request):
    selected_option = request.POST.get('option')
    print(type(selected_option))
    opt_integer = int(selected_option)
    items_to_display = range(opt_integer)
    context={
        'items_to_display':items_to_display,
    }
    return render(request,'bill_form_v2.html',context=context)

def quote(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%d/%m/%Y")
        a1=request.POST.get('a1')
        a2=request.POST.get('a2')
        a3=request.POST.get('a3')
        sub=request.POST.get('sub')
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
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        int_amountlist = [f"{locale.atof(x):,.2f}" for x in amountlist]
        float_values = [locale.atof(x) for x in int_amountlist]# Sum the floating-point numbers
        sumlist = sum(float_values)
        sumlist = locale.format_string("%.2f", sumlist, grouping=True)
        print(sumlist)
        p = inflect.engine()
        text= p.number_to_words(sumlist)
        text=text.upper()  
        combined_data = []
        for a, b, c, d, e, f in zip(desclist, hsnlist, qtylist, unitlist, ratelist,int_amountlist):
            combined_data.append({'a': a, 'b': b, 'c': c, 'd': d, 'e': e,'f':f,})

        context={
            'd':date,'a1':a1,'a2':a2,'a3':a3,'s':sub,'nof':nof,'t':text,'sum':sumlist,'combined_data':combined_data,
        }
        return render(request,'preview.html',context=context)
    
def quote2(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%d/%m/%Y")
        a1=request.POST.get('a1')
        a2=request.POST.get('a2')
        a3=request.POST.get('a3')
        sub=request.POST.get('sub')
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
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        int_amountlist = [f"{locale.atof(x):,.2f}" for x in amountlist]
        float_values = [locale.atof(x) for x in int_amountlist]# Sum the floating-point numbers
        sumlist = sum(float_values)
        sumlist = locale.format_string("%.2f", sumlist, grouping=True)
        print(sumlist)
        p = inflect.engine()
        text= p.number_to_words(sumlist)
        text=text.upper()  
        combined_data = []
        for a, b, c, d, e, f in zip(desclist, hsnlist, qtylist, unitlist, ratelist,int_amountlist):
            combined_data.append({'a': a, 'b': b, 'c': c, 'd': d, 'e': e,'f':f,})

        context={
            'd':date,'a1':a1,'a2':a2,'a3':a3,'s':sub,'nof':nof,'t':text,'sum':sumlist,'combined_data':combined_data,
        }
        return render(request,'preview2.html',context=context)
    
def b(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%d/%m/%Y")
        a1=request.POST.get('a1')
        a2=request.POST.get('a2')
        a3=request.POST.get('a3')
        sub=request.POST.get('sub')
        bno=request.POST.get('bno')
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
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        int_amountlist = [f"{locale.atof(x):,.2f}" for x in amountlist]
        float_values = [locale.atof(x) for x in int_amountlist]# Sum the floating-point numbers
        sumlist = sum(float_values)
        sumlist = locale.format_string("%.2f", sumlist, grouping=True)
        p = inflect.engine()
        text= p.number_to_words(sumlist)
        text=text.upper()  
        combined_data = []
        for a, b, c, d, e, f in zip(desclist, hsnlist, qtylist, unitlist, ratelist,int_amountlist):
            combined_data.append({'a': a, 'b': b, 'c': c, 'd': d, 'e': e,'f':f,})

        context={
            'd':date,'a1':a1,'a2':a2,'a3':a3,'s':sub,'b':bno,'nof':nof,'t':text,'sum':sumlist,'combined_data':combined_data,
        }
        return render(request,'preview3.html',context=context)
    
def b2(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        pno=request.POST.get('pno')
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%d/%m/%Y")
        a1=request.POST.get('a1')
        a2=request.POST.get('a2')
        a3=request.POST.get('a3')
        a4=request.POST.get('a4')
        sub=request.POST.get('sub')
        bno=request.POST.get('bno')
        nof=request.POST.get('nof')
        nof_int = int(nof)
        nint=int(nof)
        nof_int = range(nof_int)
        desclist=[]
        hsnlist=[]
        qtylist=[]
        ratelist=[]
        amountlist=[]
        perlist=[9 for _ in range(1,nint+1)]
        noflist=[ i for i in range(1,nint+1)]
        for i in range(len(nof_int)):
            desclist.append(request.POST.get(f'desc{i}'))
            hsnlist.append(request.POST.get(f'hsn{i}'))
            qtylist.append(request.POST.get(f'qty{i}'))
            ratelist.append(request.POST.get(f'rate{i}'))
            amountlist.append(request.POST.get(f'amount{i}'))
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        int_amountlist = [f"{locale.atof(x):,.2f}" for x in amountlist]
        slist=[int(x) for x in amountlist]
        float_values = [locale.atof(x) for x in int_amountlist]
        scgs=[int(9/100 * j) for j in float_values]
        sumscgs=sum(scgs)
        sumlist = sum(float_values)
        sumlist = locale.format_string("%.2f", sumlist, grouping=True)
        ilist=[int(g) for g in float_values]
        at=sum(slist)
        gt=(sumscgs*2)+at
        at="{:,.2f}".format(at)
        gt="{:,.2f}".format(gt)
        sumscgs="{:,.2f}".format(sumscgs)
        p = inflect.engine()
        t1=int(float(gt.replace(',','')))
        text= p.number_to_words(t1)
        text=text.upper()
        context={
            'd':date,'p':pno,'a1':a1,'a2':a2,'a3':a3,'a4':a4,'s':sub,'b':bno,'nolist':noflist,'dlist':desclist,
            'hlist':hsnlist,'qlist':qtylist,'rlist':ratelist,'alist':amountlist,'scgs':scgs,'slist':sumlist,'tex':text,
            'int_amountlist':int_amountlist,'plist':perlist,'sumscgs':sumscgs,'at':at,'gt':gt,
        }
        return render(request,'preview4.html',context=context)