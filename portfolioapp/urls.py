
from django.contrib import admin
from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('contact/', views.contact, name='contact'),
    path('contactshow/', views.contactshow, name='contactshow'),
    path('deleteContact/<int:id>', views.deleteContact, name='deleteContact'),
    path('editContact/<int:id>', views.editContact, name='editContact'),
    path('updateContact/<int:id>', views.updateContact, name='updateContact'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('testimonials/', views.testimonials, name='testimonials'),

]
