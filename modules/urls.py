from django.urls import path
from . import views

urlpatterns = [
	path('', views.moduleList, name='moduleList'),
    path('<str:pk>/', views.ModuleDetailView.as_view(), name='moduleDetail'),
	path('a', views.isCompleteView, name = 'isComplete'),
	path('aa', views.isCompleteView, name = 'isCompleteView'),


]
