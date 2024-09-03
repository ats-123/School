from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from .forms import *
import plotly.express as px
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
        a=Motivate.objects.all()
        b=[]
        for i in a:
            b.append(str(i.motivate))
        try:    
            c=b.pop()
        except:
             c=''
        ti=[]
        for i in a:
            ti.append(str(i.title))
        try:    
            ti=ti.pop()
        except:
             ti='Title'

        ann=Announcement.objects.all()
        anno=[]
        for i in ann:
            anno.append(str(i.announcement))
        try:
            annou=anno.pop()
        except:
             annou=''


        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            
            obj=Feedback()
            obj.name=name
            obj.email=email
            obj.message=message
            obj.save()
            return redirect('/')
        return render(request,"index.html",{"data":c,"title":ti,'announce':annou})
def Techlog(request):
          try:
                    if request.method=="POST":
                              name=request.POST.get("name")
                              pwd=request.POST.get("pwd")
                              q=techlog.objects.get(staffid=name)
                              if q.password==pwd:
                                        request.session['staffname']=name
                                        return redirect('dashviewteach')
                              else:
                                        return HttpResponse("incorrect password")
                    return render(request,"techlog.html")
          except:
                    
                    return render(request,"techlog.html")

def tlogout(request):
    del request.session['staffname']
    return redirect('index')
          
def dashboard(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        studName = request.POST.get('studName')
        studDept = request.POST.get('studDept')
        studPeriod = request.POST.get('studPeriod')
        status = request.POST.get('status')

        TOTAL_DAYS = 90
        status_text = "Absent" if status == "1" else "Present"

        datas=attendance()
        datas.roll_no=roll_no
        datas.subject=studPeriod
        datas.status=status_text
        datas.save()

        roll_no = int(roll_no)
        status = int(status)
        try:
            atten = attendance.objects.all().filter(roll_no=roll_no,status='Absent',subject=studPeriod)
            at=90-len(atten)
        except:
            at=90
 
        percentage = (at / TOTAL_DAYS)*100
            
        s=datetime.datetime.now()
        # print(s)
        date=s.strftime('%Y-%m-%d')
        # print(a)
        time=s.strftime('%H:%M:%S')
        # print(b)

        try:
            existing_attendance = createAttendance.objects.get(roll_no=roll_no,studPeriod=studPeriod)
            existing_attendance.studName = studName
            existing_attendance.studDept = studDept
            existing_attendance.studPeriod = studPeriod
            existing_attendance.date = date
            existing_attendance.time = time
            existing_attendance.status = status_text
            existing_attendance.percentage = percentage
            existing_attendance.save()
            
        except createAttendance.DoesNotExist:
            users=createAttendance.objects.create(roll_no=roll_no,studName=studName,studDept=studDept,
                                            studPeriod=studPeriod,date=date,time=time,status=status_text,percentage=percentage)
            

            users.save()
        # print(users)
        return redirect('dashboardGet')

    return redirect('dashboardGet')

def dashboardGet(request):
    users = createAttendance.objects.all().order_by('roll_no')
    for i in users:
         print(i.roll_no)
         data=attendance.objects.all().filter(roll_no=i.roll_no,status='Absent',subject=i.studPeriod)
         le=90-len(data)
         percentage = (le / 90)*100
         main_data=createAttendance.objects.all().get(roll_no=i.roll_no,studPeriod=i.studPeriod)
         main_data.percentage=percentage
         main_data.save()
    users = createAttendance.objects.all().order_by('roll_no')

    return render(request,'dashboard.html',{'users':users})

   

def edit(request,id):
    object=createAttendance.objects.get(id=id)
    return render(request,'edit.html',{'object':object})
    
def update(request,id):
    obj = get_object_or_404(createAttendance, id=id)
    if request.method=='POST':
        roll_no = request.POST.get('roll_no')
        studName = request.POST.get('studName')
        studDept = request.POST.get('studDept')
        studPeriod = request.POST.get('studPeriod')
        subject = request.POST.get('subject')
        # print(roll_no,studName,studDept,studPeriod,subject)
        status_text = "Absent" if studPeriod == "1" else "Present"
        obj.studName=studName
        obj.roll_no=roll_no
        obj.studDept=studDept
        obj.studPeriod=subject
        obj.status=status_text
        s=datetime.datetime.now()
        date=s.strftime('%Y-%m-%d')
        time=s.strftime('%H:%M:%S')
        obj.date=date
        obj.time=time
        try:
            if status_text=='Absent':
                 atten = attendance.objects.all().filter(roll_no=roll_no,status='Present',subject=subject)
                 dataa=atten[0]
                 dataa.status='Absent'
                 dataa.save()
            else:
                 atten = attendance.objects.all().filter(roll_no=roll_no,status='Absent',subject=subject)
                 dataa=atten[0]
                 dataa.status='Present'
                 dataa.save()
        except:
             print('not working')
        obj.save()
        return redirect ('dashboardGet')
    
    return render(request,'edit.html',{'object':obj})
def delete(request,pk):
        createAttendance.objects.filter(id=pk).delete()
        return redirect('dashboardGet')
    
def dashviewteach(request):
    if request.session['staffname'] is not None:
        staff=request.session['staffname']
        return render(request,'dashviewteach.html',{'session':staff})

def mark(request):
    if request.method=="POST":
        name=request.POST.get('user_name')
        roll=request.POST.get('roll_no')
        dep=request.POST.get('dep_name')
        tamil=request.POST.get('tamil_mark')
        english=request.POST.get('english_mark')
        maths=request.POST.get('maths_mark')
        science=request.POST.get('science_mark')
        social=request.POST.get('social_mark')
        staff=request.session['staffname']
        print(name,roll,dep,tamil,english,maths,science,social)
        tamil=int(tamil)
        english=int(english)
        maths=int(maths)
        science=int(science)
        social=int(social)

        total=tamil+english+maths+science+social
        avg=total/5
        grade=''
        if int(tamil)<40 or int(english)<40 or int(maths)<40 or int(science)<40 or int(social)<40:
            grade = "Fail"
        else:
            if avg>80 and avg<=100:
                grade="Grade A"
            elif avg>60 and avg<=80:
                grade = 'Grade B'
            elif avg>=40 and avg<=60:
                grade = 'Grade c'
            else:
                grade = 'Fail'

        obj=StuMark()
        obj.S_name=name
        obj.S_roll=roll
        obj.S_dep=dep
        obj.tamil=tamil
        obj.english=english
        obj.maths=maths
        obj.science=science
        obj.social=social
        obj.total=total
        obj.per=avg
        obj.grade=grade
        obj.staffid=staff
        obj.save()
        return redirect('mark')
        
        
    return render(request,'mark.html')

def graph(request):
    m=StuMark.objects.all()
    p=[]
    g=[]
    for i in m:
        p.append(i.S_name)
        g.append(i.grade)
    # print(p)
    # print(g)
    data={
        'Name': p,
        'Grade':g
    }
    fig = px.line(data, x='Name', y='Grade', title='Student Analysis')
    graph = fig.to_html()
    return render (request,'graph.html',{'graph':graph})

def sregister(request):
    if request.method=='POST':
        sname=request.POST.get('username')
        email=request.POST.get('email')
        stuid=request.POST.get('studentid')
        passw=request.POST.get('password')
        try:
            a=Sregister.objects.all().get(email=email)
            return render(request,'sregister.html')
        except:
            obj=Sregister()
            obj.sname=sname
            obj.email=email
            obj.stuid=stuid
            obj.passw=passw
            obj.save()
            return redirect('dashviewteach')
    return render(request,'sregister.html')

def slogin(request):
    try:
        if request.method=='POST':
            stuid=request.POST.get('stuid')
            passw=request.POST.get('password')
                
            obj=Sregister.objects.get(stuid=stuid)
            if obj.passw==passw:
                request.session['username']=obj.sname
                # print(request.session['username'])
                return redirect('studash')
            else:
                return HttpResponse("incorrect password")
        return render(request,'slogin.html')
    except:
        return render(request,'slogin.html')

def studash(request):
    if request.session['username'] is not None:
        user=request.session['username']
        return render(request,'studash.html',{'session':user})

def slogout(request):
    del request.session['username']
    return redirect('index')

def stable(request):
    a=StuMark.objects.filter(S_name=request.session['username'])
    return render (request,'stable.html',{'data':a})

def mtable(request):
    mark=StuMark.objects.filter(staffid=request.session['staffname'])
    return render(request,'mtable.html',{'data':mark})
    
def sdelete(request,pk):   
    StuMark.objects.filter(id=pk).delete()
    return redirect('mtable')

def supdate(request, id):
    if request.method=="POST":
        name=request.POST.get('user_name')
        roll=request.POST.get('roll_no')
        dep=request.POST.get('dep_name')
        tamil=request.POST.get('tamil_mark')
        english=request.POST.get('english_mark')
        maths=request.POST.get('maths_mark')
        science=request.POST.get('science_mark')
        social=request.POST.get('social_mark')
        staff=request.session['staffname']

        tamil=int(tamil)
        english=int(english)
        maths=int(maths)
        science=int(science)
        social=int(social)

        total=tamil+english+maths+science+social
        avg=total/5
        grade=''
        if int(tamil)<40 or int(english)<40 or int(maths)<40 or int(science)<40 or int(social)<40:
            grade = "Fail"
        else:
            if avg>80 and avg<=100:
                grade="Grade A"
            elif avg>60 and avg<=80:
                grade = 'Grade B'
            elif avg>=40 and avg<=60:
                grade = 'Grade c'
            else:
                grade = 'Fail'

        obj=StuMark.objects.get(id=id)
        obj.S_name=name
        obj.S_roll=roll
        obj.S_dep=dep
        obj.tamil=tamil
        obj.english=english
        obj.maths=maths
        obj.science=science
        obj.social=social
        obj.total=total
        obj.per=avg
        obj.grade=grade
        obj.staffid=staff
        obj.save()
        return redirect('mtable')
    
def sedit(request,id):
    if 'staffname' in request.session:
        object=StuMark.objects.get(id=id)
        return render(request,'supdate.html',{'object':object})

# def smarkget(request):
#     users = StuMark.objects.all().order_by('S_roll')
#     return render(request,'mark.html',{'data':users})