from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from sis.models import Schedule
from .cart import Cart
from .forms import CartAddScheduleForm

@require_POST
def cart_add(request, schedule_id):
    cart = Cart(request)
    schedule = get_object_or_404(Schedule, id=schedule_id)
    form = CartAddScheduleForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(schedule=schedule,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, schedule_id):
    cart = Cart(request)
    schedule = get_object_or_404(Schedule, id=schedule_id)
    cart.remove(schedule)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddScheduleForm(
                          initial={'quantity': item['quantity'],
                          'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})