from django.urls import path

from . import views
app_name = 'survey'

urlpatterns = [
    path('', views.Surveyhome.as_view(), name='surveyhome'),

    path('', views.Surveyworkspace.as_view(), name='surveyworkspace'),

    path('', views.Surveysidebar.as_view(), name='surveysidebar'),

    path('submit/', views.SurveySubmit.as_view(), name='surveysubmit'),
    path('yay/', views.Thanks.as_view(), name='thanks'),

]

