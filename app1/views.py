from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import ServiceSignUpForm,ServiceLogInForm,CSignupForm,CareerLogInForm,ChangePassword,CUpdateForm
from adminapp.models import Job,Team,Course,Review,ProjectSummary
from . models import ServiceSigup,CareerSignup
from MyProject import settings
from django.core.mail import send_mail
from django.contrib.auth import logout as logouts


# Create your views here.

# index page
def index(request):
    team=Team.objects.all()
    course=Course.objects.all()
    review=Review.objects.all()
    project=ProjectSummary.objects.all()
    return render(request,'index.html',{'team':team,'course':course,'review':review,'project':project})
# end of index page

# register page
def signup(request):
    if request.method=='POST':
        form=ServiceSignUpForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            designation=form.cleaned_data['Designation']
            companyname=form.cleaned_data['CompanyName']
            contactemail=form.cleaned_data['ContactEmail']
            contactnumber=form.cleaned_data['ContactNumber']
            servicetype=form.cleaned_data['ServiceType']
            servicedetails=form.cleaned_data['ServiceDetails']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']

            # Checking whether email exists or not
            user=ServiceSigup.objects.filter(ContactEmail=contactemail).exists()

            if user:
                messages.warning(request,"User exist")
                return redirect('/signup')

            elif password!=cpassword:
                messages.warning(request,"Password mismatch")
                return redirect('/signup')

            else:
                tab=ServiceSigup(Name=name,Designation=designation,CompanyName=companyname,ContactEmail=contactemail,ContactNumber=contactnumber,ServiceType=servicetype,ServiceDetails=servicedetails,Password=password)
                tab.save()
                messages.warning(request,"Signup Success")
                return redirect('/service')
    else:
        form=ServiceSignUpForm()
    return render(request,'signup.html',{'form':form})
# end of register page

# about page
def about(request):
    return render(request,'about.html')
# end of about page

# service page ( client )
def service(request):
    return render(request,'service.html')
#end of service page

# service login ( client )
def login(request):
    if request.method=='POST':
        form=ServiceLogInForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['ContactEmail']
            password=form.cleaned_data['Password']

        try:
            # checking availablity of the user
            user=ServiceSigup.objects.get(ContactEmail=email)

            # checking whether the email exists or not
            if not user:
                messages.warning(request,"User does not exist")
                return redirect('/login')
            
            # checking whether the password is correct or not
            elif password!=user.Password:
                messages.warning(request,"Incorrect Password")
                return redirect('/login')
            
            else:
                messages.warning(request,"Login success")
                return redirect('/loginhome/%s'%user.id)
        except:
            messages.warning(request,"Email or password incorrect")
            return redirect('/login')
    else:
        form=ServiceLogInForm()
    return render(request,'login.html',{'form':form})

# client home
def loginhome(request,id):
    user=ServiceSigup.objects.get(id=id)
    return render(request,'loginhome.html',{'user':user})

# signup home
def signuphome(request):
    return render(request,'signuphome.html')

# careers page
def careers(request):
    return render(request,'careers.html')

# Career signup page
def careersignup(request):
    if request.method=='POST':
        form=CSignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            email=form.cleaned_data['Email']
            cnumber=form.cleaned_data['ContactNumber']
            dob=form.cleaned_data['DOB']
            gender=form.cleaned_data['Gender']
            qualification=form.cleaned_data['Qualification']
            institutename=form.cleaned_data['InstituteName']
            yearofpass=form.cleaned_data['YearOfPassing']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']
        try:
            # Checking whether email exists or not
            user=CareerSignup.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"User exist")
                return redirect('/careersignup')

            elif password!=cpassword:
                messages.warning(request,"Password mismatch")
                return redirect('/careersignup')

            else:
                tab=CareerSignup(Name=name,Email=email,ContactNumber=cnumber,DOB=dob,Gender=gender,Qualification=qualification,InstituteName=institutename,YearOfPassing=yearofpass,Password=password)
                tab.save()
                messages.warning(request,"Signup Success")
                return redirect('/careers')
        except:
            messages.warning(request,"Error on data..please double check")        
    else:
        form=CSignupForm()
    return render(request,'careersignup.html',{'form':form})

# Career login ( Job seekers )
def clogin(request):
    if request.method=='POST':
        form=CareerLogInForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
        try:
            # checking availablity of the user
            user=CareerSignup.objects.get(Email=email)

            # checking whether the email exists or not
            if not user:
                messages.warning(request,"User does not exist")
                return redirect('/clogin')
            
            # checking whether the password is correct or not
            elif password!=user.Password:
                messages.warning(request,"Incorrect Password")
                return redirect('/clogin')
            
            else:
                messages.warning(request,"Login success")
                return redirect('/chome/%s'%user.id)
        except:
            messages.warning(request,"Email or password error")
    else:
        form=CareerLogInForm()
    return render(request,'clogin.html',{'form':form})

# career home
def chome(request,id):
    user=CareerSignup.objects.get(id=id)
    job=Job.objects.all()
    return render(request,'chome.html',{'user':user,'job':job})

# contact page
def contact(request):
    return render(request,'contact.html')

# mail
def mail(request):
    if request.method=='POST':
        cname=request.POST.get('contact_name')
        cemail=request.POST.get('contact_email')
        cmessage=request.POST.get('contact_message')
        toemail='amalraj0310@gmail.com'
        res = send_mail(cname,cmessage,settings.EMAIL_HOST_USER,[toemail],fail_silently=False)
        if(res==1):
            msg="Mail sent successfully"
        else:
            msg="Message could not sent"
        return HttpResponse(msg)
    else:
        return render(request,'index.html')

# logout
def logout(request):
    logouts(request)
    messages.warning(request,"Logout success")
    return redirect('/')

# change password for clients
def changepassword(request,id):
    user=CareerSignup.objects.get(id=id)
    if request.method=='POST':
        form=ChangePassword(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']

            if oldpassword!=user.Password:
                messages.warning(request,"Incorrect Password")
                return redirect('/changepassword/%s'%user.id)
            elif oldpassword==newpassword:
                messages.warning(request,"Password not available")
                return redirect('/changepassword/%s'%user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,"Password Mismatch")
                return redirect('/changepassword/%s'%user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.warning(request,"Success")
                return redirect('/clogin')
    else:
        form=ChangePassword()
    return render(request,'changepassword.html',{'form':form,'user':user})

# Update page for career
def cupdate(request,id):
    user=CareerSignup.objects.get(id=id)
    if request.method=='POST':
        form=CUpdateForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Success")
            return redirect('/chome/%s'%user.id)
    else:
      form=CUpdateForm(instance=user)
    return render(request,'cupdate.html',{'form':form,'user':user})