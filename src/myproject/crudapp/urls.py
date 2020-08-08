from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home_view,name='nhome'),
    path('sportal/',views.form_view,name='nform'),
    path('sportal/sdetail/',views.detail_view,name='ndetail'),
    path('sdetail/<int:pk>/edit',views.edit_view,name='nedit'),
    path('sdetail/<int:pk>/delete/',views.delete_view,name='ndelete'),
]