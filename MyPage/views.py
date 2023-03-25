from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_sameorigin
def home (request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())
