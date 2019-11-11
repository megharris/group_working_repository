from decimal import Decimal
from django.conf import settings
from sis.models import Schedule

class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, schedule, quantity=1, update_quantity=False):
        """
        Add a schedule to the cart or update its quantity.
        """
        schedule_id = str(schedule.schedule_id)
        if schedule_id not in self.cart:
            self.cart[schedule_id] = {'quantity': 0,
                                     'price': str(schedule.price)}
        if update_quantity:
            self.cart[schedule_id]['quantity'] = quantity
        else:
            self.cart[schedule_id]['quantity'] += quantity
        self.save()

    def remove(self, schedule):
        """
        Remove a schedule from the cart.
        """
        schedule_id = str(schedule.schedule_id)
        if schedule_id in self.cart:
            del self.cart[schedule_id]
            self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and get the schedules
        from the database.
        """
        schedule_ids = self.cart.keys()
        # get the schedule objects and add them to the cart
        schedules = Schedule.objects.filter(id__in=schedule_ids)

        cart = self.cart.copy()
        for schedule in schedules:
            cart[str(schedule.schedule_id)]['schedule'] = schedule

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()