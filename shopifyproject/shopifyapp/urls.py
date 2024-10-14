from django.urls import path
from . import views

app_name = 'shopifyapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:c_slug>/',views.index,name='category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proDetail'),
    path('searchresult',views.SearchResult,name='SearchResult'),
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),
]