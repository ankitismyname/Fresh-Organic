
from django.contrib import admin
from django.urls import path, include
from Userdata import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('main.html', views.home,name="home"),
    path('flowers.html',views.flowers),
    path('furits.html',views.furits),
    path('vegetable.html',views.vegetables),
    path('dryfurits.html',views.dryfurits),
    path('contact.html',views.contact),
    path('about.html',views.about),
    path('signup.html',views.signup,name='signup'),
    path('login.html',views.user_login,name='login'),
    path('personal.html',views.personal,name='personal'),
    path('logout/',views.logout_user,name="logout"),
    path('changepswd.html',views.change_password,name='changepswd'),
    path('editprofile.html',views.editprofile),
    path('products/', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),


]

