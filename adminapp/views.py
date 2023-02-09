from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import AdminPageForm,SUpdate,ACUpdate,Addjob,AddTeam,AddCourse,JobEdit,AddReview,TeamEdit,CourseEdit,ReviewEdit,PSEdit
from . models import AdminPage,Job,Team,Course,Review,ProjectSummary
from app1.models import ServiceSigup,CareerSignup
from MyProject import settings

# Create your views here.

# admin login
def adminlogin(request):
    if request.method=='POST':
        form=AdminPageForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['UserId']
            password=form.cleaned_data['Password']
        try:
            # checking availablity of the user
            user=AdminPage.objects.get(UserId=email)

            # checking whether the email exists or not
            if not user:
                messages.warning(request,"User does not exist")
                return redirect('/adminlogin')
            
            
            # checking whether the password is correct or not
            elif password!=user.Password:
                messages.warning(request,"Incorrect Password")
                return redirect('/adminlogin')
            
            else:
                messages.warning(request,"Login success")
                return redirect('/adminloginhome/%s'%user.id)
        except:
            messages.warning(request,"Userid or password error")
    else:
        form=AdminPageForm()
    return render(request,'adminlogin.html',{'form':form})

# adminloginhome
def adminloginhome(request):
    users=ServiceSigup.objects.all()
    users1=CareerSignup.objects.all()
    job=Job.objects.all()
    team=Team.objects.all()
    course=Course.objects.all()
    review=Review.objects.all()
    project=ProjectSummary.objects.all()
    return render(request,'adminloginhome.html',{'users':users,'users1':users1,'job':job,'team':team,'course':course,'review':review,'project':project})

# delete controll access for admin(clients)
def delete(request,id):
    user=ServiceSigup.objects.get(id=id)
    user.delete()
    messages.warning(request,"Removed successfully !")
    return redirect('/adminloginhome/1')

# delete controll access for admin (career)
def delete1(request,id):
    user=CareerSignup.objects.get(id=id)
    user.delete()
    messages.warning(request,"Removed successfully !")
    return redirect('/adminloginhome/1')

# admin update (client's details)
def supdate(request,id):
    user=ServiceSigup.objects.get(id=id)
    if request.method=='POST':
        form=SUpdate(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Update Successful !")
            return redirect('/adminloginhome/1')
    else:
      form=SUpdate(instance=user)
    return render(request,'supdate.html',{'form':form,'user':user})


# admin update (career details)
def acupdate(request,id):
    user=CareerSignup.objects.get(id=id)
    if request.method=='POST':
        form=ACUpdate(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Update Successful")
            return redirect('/adminloginhome/1')
    else:
      form=ACUpdate(instance=user)
    return render(request,'acupdate.html',{'form':form,'user':user})

# Job add page
def addjob(request):
    if request.method=='POST':
        form=Addjob(request.POST)
        if form.is_valid():
            title=form.cleaned_data['Title']
            location=form.cleaned_data['Location']
            description=form.cleaned_data['Decsription']
            date=form.cleaned_data['Date']

            tab=Job(Title=title,Location=location,Decsription=description,Date=date)
            tab.save()
            messages.warning(request,"Job added Successfully")
            return redirect('/adminloginhome/1')
    else:
        form=Addjob()
    return render(request,'addjob.html',{'form':form})

# Team details adding page
def addteam(request):
    if request.method=='POST':
        form=AddTeam(request.POST or None,request.FILES or None)
        if form.is_valid():
            image=form.cleaned_data['Image']
            name=form.cleaned_data['Name']
            designation=form.cleaned_data['Designation']

            tab=Team(Image=image,Name=name,Designation=designation)
            tab.save()
            messages.warning(request,"Team updated Successfully !")
            return redirect('/adminloginhome/1')
    
    else:
        form=AddTeam()
    return render(request,'addteam.html',{'form':form})

# delete controll access for admin (career)
def jobdelete(request,id):
    user=Job.objects.get(id=id)
    user.delete()
    messages.warning(request,"Removed successfully")
    return redirect('/adminloginhome/1')

# Add course page
def addcourse(request):
    if request.method=='POST':
        form=AddCourse(request.POST or None,request.FILES or None)
        if form.is_valid():
            photo=form.cleaned_data['Photo']
            course=form.cleaned_data['Course']
            name=form.cleaned_data['Name']

            tab=Course(Photo=photo,Course=course,Name=name)
            tab.save()
            messages.warning(request,"Course Added Successfully !")
            return redirect('/adminloginhome/1')
        
    else:
        form=AddCourse()
    return render(request,'addcourse.html',{'form':form})

# Job edit page
def jobedit(request,id):
    user=Job.objects.get(id=id)
    if request.method=='POST':
        form=JobEdit(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Job Updated Successfully")
            return redirect('/adminloginhome/1')
    else:
      form=JobEdit(instance=user)
    return render(request,'jobedit.html',{'form':form,'user':user})

# review adding page
def addreview(request):
    if request.method=='POST':
        form=AddReview(request.POST or None,request.FILES or None)
        if form.is_valid():
            review=form.cleaned_data['Review']
            photo=form.cleaned_data['Photo']
            name=form.cleaned_data['Name']
            cname=form.cleaned_data['CompanyName']

            tab=Review(Review=review,Photo=photo,Name=name,CompanyName=cname)
            tab.save()
            messages.warning(request,"Review Added Successfully !")
            return redirect('/adminloginhome/1')
        
    else:
        form=AddReview()
    return render(request,'addreview.html',{'form':form})

# Team edit page
def teamedit(request,id):
    user=Team.objects.get(id=id)
    if request.method=='POST':
        form=TeamEdit(request.POST or None,request.FILES,  instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Team Updated Successfully")
            return redirect('/adminloginhome/1')
    else:
      form=TeamEdit(instance=user)
    return render(request,'teamedit.html',{'form':form,'user':user})

# Team delete control
def teamdel(request,id):
    user=Team.objects.get(id=id)
    user.delete()
    messages.warning(request,"Removed successfully")
    return redirect('/adminloginhome/1')


# Course edit page
def courseedit(request,id):
    user=Course.objects.get(id=id)
    if request.method=='POST':
        form=CourseEdit(request.POST or None,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Course Updated Successfully")
            return redirect('/adminloginhome/1')
    else:
      form=CourseEdit(instance=user)
    return render(request,'courseedit.html',{'form':form,'user':user})

# Course delete control
def coursedel(request,id):
    user=Course.objects.get(id=id)
    user.delete()
    messages.warning(request,"Removed successfully")
    return redirect('/adminloginhome/1')

# Review edit page
def reviewedit(request,id):
    user=Review.objects.get(id=id)
    if request.method=='POST':
        form=ReviewEdit(request.POST or None,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Review Updated Successfully !")
            return redirect('/adminloginhome/1')
    else:
        form=ReviewEdit(instance=user)
    return render(request,'reviewedit.html',{'form':form})

# admin update (career details)
def psedit(request,id):
    user=ProjectSummary.objects.get(id=id)
    if request.method=='POST':
        form=PSEdit(request.POST or None,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Update Successful")
            return redirect('/adminloginhome/1')
    else:
      form=PSEdit(instance=user)
    return render(request,'psedit.html',{'form':form,'user':user})

# Review delete page
def revdel(request,id):
    user=Review.objects.get(id=id)
    user.delete()
    messages.warning(request,"Removed successfully")
    return redirect('/adminloginhome/1')
