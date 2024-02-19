from django.shortcuts import render
from django.contrib import messages,auth
from django.template import Template, Context
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Student
from .forms import StudentRegister
from .forms import StudentLogin
from .models import StudentEnrolled
from .models import Teacher
from .models import TeacherTeaches
from .models import FeedbackCsn209
from .models import FeedbackCsn211
# Create your views here.

def changepassword(request):
    if request.method=='POST':
        sid=request.POST['sid']
        print(sid)


    return render(request,'feedback/changepassword.html',{})



def feedback_resultCSN209(request):
    allobjects = FeedbackCsn209.objects.all()

    list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    count = 0
    for objects in allobjects:
        count = count + 1
        list[0] = list[0] + objects.q1
        list[1] = list[1] + objects.q2
        list[2] = list[2] + objects.q3
        list[3] = list[3] + objects.q4
        list[4] = list[4] + objects.q5
        list[5] = list[5] + objects.q6
        list[6] = list[6] + objects.q7
        list[7] = list[7] + objects.q8

    for i in range(8):
        list[i] = list[i] / count

    context = {
        "list": list,
        "objects": allobjects,
    }

    return render(request, 'feedback/feedback_resultcsn209.html', context)

def feedback_resultCSN211(request):
    allobjects=FeedbackCsn211.objects.all()
    list=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    count=0
    for objects in allobjects:
        count=count+1
        list[0]=list[0]+objects.q1
        list[1] = list[1]+objects.q2
        list[2] = list[2]+objects.q3
        list[3] = list[3]+objects.q4
        list[4] = list[4]+objects.q5
        list[5] = list[5]+objects.q6
        list[6]=list[6]+objects.q7
        list[7] = list[7]+objects.q8

    for i in range(8):
        list[i]=list[i]/count

    context={
        "list" : list,
        "objects": allobjects,
    }

    return render(request, 'feedback/feedback_resultcsn211.html', context)

def feedbackCSN211(request):
    query = request.GET.get('id')
    query=int(query)
    if request.method == 'POST':
        q1 = request.POST['Q1']
        q2=request.POST['Q2']
        q3 = request.POST['Q3']
        q4 = request.POST['Q4']
        q5 = request.POST['Q5']
        q6 = request.POST['Q6']
        q7 = request.POST['Q7']
        q8 = request.POST['Q8']
        q1= int(q1)
        q2=int(q2)
        q3 = int(q3)
        q4 = int(q4)
        q5 = int(q5)
        q6 = int(q6)
        q7 = int(q7)
        q8 = int(q8)
        FeedbackCsn211.objects.create(sid=query,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8)
        return HttpResponse("Congrats you have filled the feedback form for Machine Learning ")

    return render(request, 'feedback/feedbackcsn211.html',{})

def feedbackCSN209(request):
    query = request.GET.get('id')
    query=int(query)
    if request.method == 'POST':
        q1 = request.POST['Q1']
        q2=request.POST['Q2']
        q3 = request.POST['Q3']
        q4 = request.POST['Q4']
        q5 = request.POST['Q5']
        q6 = request.POST['Q6']
        q7 = request.POST['Q7']
        q8 = request.POST['Q8']
        q1= int(q1)
        q2=int(q2)
        q3 = int(q3)
        q4 = int(q4)
        q5 = int(q5)
        q6 = int(q6)
        q7 = int(q7)
        q8 = int(q8)
        FeedbackCsn209.objects.create(sid=query,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8)
        return HttpResponse("Congrats you have filled the feedback form for operating systems ")

    return render(request, 'feedback/feedbackcsn209.html',{})



def student_login_view(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        password = request.POST['pass']
        user= Student.objects.filter(sid=sid, password=password)
        if user.exists():
            obj = Student.objects.get(sid=sid, password=password)
            courses = StudentEnrolled.objects.filter(sid=sid)
            context = {
                "object": obj,
                "courses": courses
            }
            return render(request, 'feedback/studentlogin1.html', context)
        else:
            return HttpResponse('User does not exist please register <a href="/student_login/register/"> Visit this link to register</a>')


    return render(request,'feedback/studentlogin.html')




def student_form_view(request):
    form= StudentRegister()
    if request.method == 'POST' :
        form = StudentRegister(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponse('<h3> Your account has been created now go to login page </h3><br> <a href="/student_login/login/">login page</a>')

    context={
        "form" : form
    }
    return render(request,'feedback/student_register.html',context)



def teacher_login(request):
    if request.method == 'POST':
        tid = request.POST['tid']
        password = request.POST['pass']
        print(tid,password)
        user= Teacher.objects.filter(tid=tid, password=password)
        if user.exists():
            obj = Teacher.objects.get(tid=tid, password=password)
            courses = TeacherTeaches.objects.filter(tid=tid)
            context = {
                "object": obj,
                "courses": courses
            }
            return render(request, 'feedback/teacher_login1.html', context)
        else:
            return HttpResponse('User does not exist please ask the admin to register your account')


    return render(request,'feedback/teacher_login.html')



def home(request):
    # invoke render shortcut to create HttpResponse object with template html file.
    return render(request,'feedback/home.html',{})

def student_login(request):
    print(request.user)
    # invoke render shortcut to create HttpResponse object with template html file.
    resp = render(request,'feedback/student_login.html',{})
    # set response headers and values.
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    return resp

def t_c(request):
# invoke render shortcut to create HttpResponse object with template html file.
    resp = render(request,'feedback/t&c.html')
    # set response headers and values.
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    return resp

