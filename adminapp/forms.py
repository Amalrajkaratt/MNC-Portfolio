from django import forms
from .models import AdminPage,Job,Team,Course,Review,ProjectSummary
from app1.models import ServiceSigup,CareerSignup

# Admin page
class AdminPageForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=15)
    class Meta():
        model=AdminPage
        fields=('UserId','Password')


# Client's Update for admin
class SUpdate(forms.ModelForm):
    class Meta():
        model=ServiceSigup
        fields='__all__'

# Career Update for admin
class ACUpdate(forms.ModelForm):
    class Meta():
        model=CareerSignup
        fields='__all__'

# Add job
class Addjob(forms.ModelForm):
    class Meta():
        model=Job
        fields='__all__'

# Adding team
class AddTeam(forms.ModelForm):
    class Meta():
        model=Team
        fields='__all__'

# Adding team
class AddCourse(forms.ModelForm):
    class Meta():
        model=Course
        fields='__all__'
    
# Job Edit for admin
class JobEdit(forms.ModelForm):
    class Meta():
        model=Job
        fields='__all__'

# Adding Review
class AddReview(forms.ModelForm):
    class Meta():
        model=Review
        fields='__all__'

# Team Edit for admin
class TeamEdit(forms.ModelForm):
    class Meta():
        model=Team
        fields='__all__'

# Team Edit for admin
class CourseEdit(forms.ModelForm):
    class Meta():
        model=Course
        fields='__all__'

# Review edit for admin
class ReviewEdit(forms.ModelForm):
    class Meta():
        model=Review
        fields='__all__'

# Project Summary edit for admin
class PSEdit(forms.ModelForm):
    class Meta():
        model=ProjectSummary
        fields='__all__'
