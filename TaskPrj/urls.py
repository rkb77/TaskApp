from django.contrib import admin
from django.urls import path, include
from Task_App import views as taskappviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', taskappviews.index, name='index'),
    path('account/', include('users_App.urls')),
    path('task/', include('Task_App.urls')),
    path('contact', taskappviews.contact, name='contact'),
    path('about-us', taskappviews.about, name='about'),
]