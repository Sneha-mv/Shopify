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
    path('add/<int:product_id>',views.add_cart,name='add_cart'),
    path('cart_detail',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>',views.full_remove,name='full_remove'),
]