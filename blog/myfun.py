from django.shortcuts import HttpResponse,render

import json
def index_page(r):
    text ="<h1 style='color:red'>hello World ! </h1>This is my Index Page"
    text1 =['Ram',1220]
    mydic ={"name":"Aman",'text':text,'text1':text1}
    return HttpResponse(json.dumps(mydic))

def about_page(request):
    return HttpResponse('about page')

def home(obj):
    return render(obj,'home.html')

def service(request):
    salary =50000
    emp_list = ["Ram","Mohan","sohan"]
    myemp ={'name':"Ram","salary":5000}
    text ={"text1":"My Text is simple Text",
           'sal':salary,
           'emplist':emp_list,
           'edata':myemp}

    return render(request,'includes/service.html',text)


def demo_view(request):
    mydict ={}
    # print(request.method)
    # print(request.GET)
    # print(request.GET.get('txt1'))
    # name1 =request.GET.get('name')
    # salary1 =request.GET.get('salary')
    # print(name1,salary1)
    # mydict['name']=name1
    plist = {'pizza1': 600, 'pizza2': 800}
    print(request.method)
    print(request.POST)
    name =request.POST.get('name')
    salary1 =request.POST.get('salary')

    mydict['name']=name
    mydict.update({'sly':salary1})
    mydict['plist']=plist



    return render(request,'demo.html',mydict)



def login_view(request):
    mydict =dict()
    mylist =[55,55,55,5,587,99,]
    mydict['ml']=mylist
    if request.method ==  'POST':
        username =request.POST.get('uname')
        password =request.POST.get('upass')
        print(username,password)
        mydict['un']=username
        mydict['pw']=password
    return render(request,'login.html',mydict)

