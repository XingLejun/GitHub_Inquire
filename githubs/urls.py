from django.urls import path
from githubs import views

urlpatterns = [
	path('',views.index,name='index'),

	path('user',views.user, name='user'),
]

