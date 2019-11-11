from django import forms

SCHEDULE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddScheduleForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=SCHEDULE_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)