# coding=utf-8
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm

from randomizer import settings


#Source: http://lincolnloop.com/blog/2008/may/10/getting-requestcontext-your-templates/
def render_to(template_name):
  def renderer(func):
    def wrapper(request, *args, **kw):
      output = func(request, *args, **kw)
      if not isinstance(output, dict):
        return output
      output.update({"settings": settings, "request": request})
      if not "auth_form" in output:
        output["auth_form"] = AuthenticationForm()
      return render_to_response(template_name, output, context_instance=RequestContext(request))
    return wrapper
  return renderer


def is_ajax(func, message = "is not a ajax request"):
  def wrapper(request, *args, **kw):
    if not request.is_ajax(): raise Http404(message)
    return func(request, *args, **kw)
  return wrapper