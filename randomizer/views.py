from misc.decorator import render_to
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.core.context_processors import csrf

from randomizer.forms import MainForm
from randomizer import *

@ensure_csrf_cookie
@render_to("index.html")
def index(request):
  output = csrf(request)
  output.update({
    "names": NAMES[:2],
    "not_in_game": NAMES[2:],
    "nations":NATIONS})
  print output
  return output



@ensure_csrf_cookie
@render_to("update.html")
def update(request):
  return csrf(request)



@csrf_protect
def get_update(request):
  if request.method != "POST":
    raise Http404
  else:
    return HttpResponse("OK")

@csrf_protect
def submit(request):
  if request.method != "POST":
    raise Http404
  else:
    return HttpResponse("OK")