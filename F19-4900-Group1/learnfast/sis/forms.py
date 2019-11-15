from django import forms
from .models import Course, Tutor
from django.contrib.auth.models import User, Group

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_description', 'course_subject')

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('tutor_name', 'tutor_address', 'tutor_city', 'tutor_zip', 'tutor_email', 'tutor_phone', 'tutor_sub_expertise')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



