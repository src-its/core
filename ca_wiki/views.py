from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Issue

def index(request):
    new_issues = Issue.objects.order_by('-issue_opened')
    template = loader.get_template('ca_wiki/index.html')
    context = RequestContext(request, {
            'new_issues': new_issues,
    })
    return HttpResponse(template.render(context))
    # return HttpResponse("Welcome to the CA Wiki. Here's some text while we \
    #        figure out how to serve a page.")
    
