from django.shortcuts import render
from django.views.generic import DetailView
from django import forms
from .get_lots import *


class LocationForm(forms.Form):
    location = forms.CharField(max_length=100)


class ViewRatings(DetailView):
    template_name = 'ratings/ratings.html'
    initial = {'key': 'value'}
    form_class = LocationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        location = None
        if form.is_valid():
            location = request.POST['location']

        results = search(location)
        return render(request, self.template_name, {"form": form, "results": results})
