from django.urls import path

from . import views 
app_name = 'explore'

urlpatterns = [

    path('', views.ExploreHome.as_view(), name='explorehome'),
    path('', views.Expworkspace.as_view(), name='expworkspace'),
    path('', views.Expsidebar.as_view(), name='expsidebar'),
    path('surveyresponses/', views.SurveyHome.as_view(), name='responsehome'),
    path('surveyresponses/list/', views.SurveyListView.as_view(), name='responselist'),
    path('surveyresponses/yr/<int:year>/', views.SurveyYearView.as_view(), name='responsesbyyear'),
    path('surveyresponse/<int:pk>/', views.SurveyResponseView.as_view(), name='responsedetail')
    
   
]

