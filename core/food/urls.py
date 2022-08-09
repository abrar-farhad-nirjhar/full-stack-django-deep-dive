from django.urls import path
from food.views import *

app_name = 'food'

urlpatterns = [
    path('', index, name='index'),
    path('item/', item, name="item"),
    path('item/<int:id>/', detail, name="item-detail"),
    # add items
    path('add', create_item, name="create-item"),
    path('edit/<int:id>', update, name="update-item"),
    path('delete/<int:id>', delete, name="delete-item"),

]
