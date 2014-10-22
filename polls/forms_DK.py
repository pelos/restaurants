from django import forms
from polls.models import Restaurant
from polls.models import Person
from polls.models import Dish
import django
django.setup()


class NameForm(forms.Form):
    your_email = forms.EmailField(initial="a@b.com")
#    django.setup()

    all = Restaurant.objects.all()

    options_ratio = []
    for i in all:
        mini_list = []
        mini_list.append(i.id)
        mini_list.append(i.name)
        options_ratio.append(mini_list)

    ratio = forms.ChoiceField(choices=options_ratio, widget=forms.RadioSelect(), initial=1)


class FormRegistration(forms.ModelForm):
    class Meta:
        model = Person


class FormDishes(forms.Form):
    your_email = forms.EmailField(initial="a@b.com")
    ratiooo = forms.ChoiceField(choices="", widget=forms.RadioSelect(), initial=1)

    def __init__(self, *args, **kwargs):
        self.restaurant_id = kwargs.pop("restaurant_id")
        super(FormDishes, self).__init__(*args, **kwargs)
        self.fields["ratiooo"].choices = self.make_choices()

    def make_choices(self):
        all = Dish.objects.filter(restaurant_id=self.restaurant_id)
        options_ratio = []
        for i in all:
            options_ratio.append((i.id, i.name))
        return options_ratio
