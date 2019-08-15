from django.urls import path
from . import views

app_name = 'ticketing'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('ticket/<int:ticket_num>/', views.ticket_detail, name='ticket_detail')
]
