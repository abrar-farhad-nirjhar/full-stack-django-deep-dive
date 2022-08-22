from django.forms import ModelForm
from food.models import *


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
