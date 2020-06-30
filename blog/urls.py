
from django.contrib import admin
from django.urls import path

# from .myfun import index_page,about_page,home,service
from . import myfun as views
# from .myfun import demo_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_page),
    path('about/',views.about_page),
    path('home/',views.home),
    path('s/',views.service),
    path('demo/',views.demo_view),
    path('login/', views.login_view),

]
