from django import forms
from .models import Course, Tutor

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_description', 'course_subject')

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('tutor_name', 'tutor_address', 'tutor_city', 'tutor_zip', 'tutor_email', 'tutor_phone', 'tutor_sub_expertise')



