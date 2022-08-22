from django.urls import path
from food.views import *

app_name = 'food'

urlpatterns = [
    path('', IndexClassView.as_view(), name='index'),
    path('item/', item, name="item"),
    path('item/<int:pk>/', FoodDetail.as_view(), name="item-detail"),
    # add items
    path('add', CreateItem.as_view(), name="create-item"),
    path('edit/<int:id>', update, name="update-item"),
    path('delete/<int:id>', delete, name="delete-item"),

]
