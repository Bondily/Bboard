from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns= [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('accounts/login', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page='bboard:index',template_name='registration/logout.html'), name='logout')

]
