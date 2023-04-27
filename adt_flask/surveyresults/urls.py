from django.urls import path

from . import views
app_name = 'surveyresults'

urlpatterns = [
    path('', views.SRhome.as_view(), name='sr_home'),
    path('', views.SRworkspace.as_view(), name='sr_work'),
    path('', views.SRsidebar.as_view(), name='sr_sidebar'),
    path('<int:pk>/', views.SRdetail.as_view(), name='responsedetail')
]

