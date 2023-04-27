from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from adt_flask.models import SurveyResponse

class ExploreHome(generic.TemplateView):
    template_name = 'explore/explorehome.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countresponse'] = SurveyResponse.objects.count()
        return context
  
class Expworkspace(generic.TemplateView):
    template_name = 'explore/expworkspace.html'
  

class Expsidebar(generic.TemplateView):
    template_name = 'explore/expsidebar.html'
    

class SurveyHome(generic.ListView):
    template_name = 'explore/responsehome.html'
    context_object_name = 'responsehome'
    paginate_by = 25
    def get_queryset(self):
        return SurveyResponse.objects.filter(year__lte=2017).order_by('id')
        
class SurveyListView(generic.ListView):
    template_name = 'explore/responselist.html'
    context_object_name = 'responselist'
    paginate_by = 25

    def get_queryset(self):
        return SurveyResponse.objects.filter(year__lte=2017).order_by('id')

class SurveyResponseView(generic.DetailView):
    model = SurveyResponse
    context_object_name = 'response'
    template_name = 'explore/responsedetail.html'


class SurveyYearView(generic.ListView):
    model = SurveyResponse
    template_name = 'explore/responsesbyyear.html'
    context_object_name = 'responsehome'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        return context

    def get_queryset(self):
        year = self.kwargs['year']
        return SurveyResponse.objects.filter(year=year).order_by('id')
