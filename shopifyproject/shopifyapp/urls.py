from django.urls import path
from . import views

app_name = 'shopifyapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:c_slug>/',views.index,name='category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proDetail'),
]