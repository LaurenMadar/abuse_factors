import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

from adt_flask.models import SurveyResponse
from .forms import SurveyForm

class Surveyhome(generic.TemplateView):
    template_name = 'survey/surveyhome.html'


class Surveyworkspace(FormView):
    template_name = 'survey/surveyworkspace.html'
    form_class = SurveyForm

    def form_valid(self, form):
        #form.save(commit=True)
        return super().form_valid(form)


class Surveysidebar(generic.TemplateView):
    template_name = 'survey/surveysidebar.html'

class SurveySubmit(FormView):
    model = SurveyResponse
    exclude = ["id"]
    template_name = 'survey/surveyresponse_form.html'
    form_class = SurveyForm

    success_url = "../yay/"

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data()
        return context

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=True)
        context = self.get_context_data()
        context['newid'] = obj.pk
        context['response'] = SurveyResponse.objects.get(pk=obj.pk)
        return render(self.request, 'survey/yay.html', context)

class Thanks(generic.DetailView):
    model = SurveyResponse
    template_name = 'survey/yay.html'
    #context_object_name = 'response'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        id = context['newid']
        return SurveyResponse.objects.get(pk=id)
