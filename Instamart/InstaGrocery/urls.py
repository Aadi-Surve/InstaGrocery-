from django.urls import path
from InstaGrocery import views



urlpatterns = [
    path("", views.home, name="home"),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'), #URL pattern for editing a product
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]   

