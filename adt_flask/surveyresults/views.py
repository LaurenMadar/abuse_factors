from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from adt_flask.models import SurveyResponse

class SRhome(generic.ListView):
    template_name = 'surveyresults/sr_home.html'
    context_object_name = 'responses'
    paginate_by = 25
    model = SurveyResponse
    def get_queryset(self):
        return SurveyResponse.objects.filter(year__gt=2017).order_by('id')

class SRworkspace(generic.ListView):
    template_name = 'surveyresults/sr_workspace.html'
    success_url = "../yay/"
    model = SurveyResponse
    exclude = ["id"]



class SRsidebar(generic.TemplateView):
    template_name = 'surveyresults/sr_sidebar.html'

class SRdetail(generic.DetailView):
    model = SurveyResponse
    context_object_name = 'response'
    template_name = 'surveyresults/responsedetail.html'


