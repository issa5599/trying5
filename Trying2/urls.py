from django.urls import path,re_path
from.import views
from django.views.generic.base import RedirectView


app_name='Trying2'
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
urlpatterns = [
    path('', views.base,name='base'),
    path('<int:lesson_id>/', views.temp1,name='temp1'),
    path('<int:lesson_id>/', views.super,name='super'),
    re_path(r'^favicon\.ico$', favicon_view),
]