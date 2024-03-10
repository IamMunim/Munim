from django.urls import path
from .import views

urlpatterns=[
    path('',views.homePage,name='home'),
    path('project/<str:pk>', views.projectPage,name='project'),
    path('add-project/',views.addProject,name='add-project'),
    path('all-project/',views.projectAll,name='all-project'),
    path('edit-project/<str:pk>/', views.editProject, name="edit-project"),
    path('inbox/',views.inboxPage,name='inbox'),
    path('contact/',views.contactPage,name='contact'),
    path('message/<str:pk>/',views.messagePage,name='message'),


]