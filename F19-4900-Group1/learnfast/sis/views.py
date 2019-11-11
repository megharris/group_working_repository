from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from cart.forms import CartAddScheduleForm

now = timezone.now()
def home(request):
    return render(request, 'sis/home.html', {'sis':home})

@login_required
def tutor_list(request):
    tutor = Tutor.objects.filter(created_date__lte=timezone.now())
    return render(request, 'sis/tutor_list.html', {'tutors': tutor})

@login_required
def course_list(request):
    course = Course.objects.filter(created_date__lte=timezone.now())
    return render(request, 'sis/course_list.html', {'courses': course})

@login_required
def schedule_list(request):
    #schedule = Schedule.objects.filter(created_date__lte=timezone.now())
    schedules = Schedule.objects.filter(available=True)
    return render(request, 'sis/schedule_list.html', {'schedules': schedules})

@login_required
def schedule_detail(request, schedule_id, slug):
    schedule = get_object_or_404(Schedule, schedule_id=schedule_id, slug=slug, available=True)
    cart_schedule_form = CartAddScheduleForm()
    return render(request,'sis/schedule_detail.html', {'schedule': schedule, 'cart_schedule_form': cart_schedule_form})
