from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.views import View
from .forms import PrayerRequestForm
from .models import (
    Website,
    FAQ,
    PrayerRequest,
    )

class Index(TemplateView):
    template_name = 'core/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['webinfo'] = get_object_or_404(Website)
        return context

class AboutUs(Index):
    template_name = 'core/about.html'

class ContactUs(View):
    pass

class FAQView(ListView):
    template_name = 'core/faq.html'
    queryset = FAQ.objects.all()[:20]
    context_object_name = 'faqs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['webinfo'] = get_object_or_404(Website)
        return context

class PrayerRequestView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {'form': PrayerRequestForm()}
        self.template_name = 'core/prayer-request.html'

    def get(self, request):
        return render(request,self.template_name,self.context)

    def post(self, request):
        form_data = PrayerRequestForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Your prayer request has been successfully sent")
            return HttpResponseRedirect(reverse('core:prayer_request'))
        else:
            self.context = {'form': form_data}
            messages.error(request,"An error occured while submitting your form. Please try again.")
            
            return render(request, self.template_name, self.context)


class PrayerRequestList(ListView):
    queryset = PrayerRequest.objects.all().order_by('-timestamp')
    template_name = 'core/prayer-request-list.html'
    context_object_name = 'prayer_requests'
