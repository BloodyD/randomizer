from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

from django.utils import simplejson
from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib.auth.forms import AuthenticationForm

from misc.decorator import render_to, is_ajax
from randomizer.forms import MainForm
from randomizer import *

import traceback

@ensure_csrf_cookie
@render_to("index.html")
def index(request):
  output = csrf(request)
  output.update({
    "names": NAMES[:2],
    "not_in_game": NAMES[2:],
    "nations":NATIONS})
  return output


@require_POST
@render_to("index.html")
def login(request):
  form = AuthenticationForm(data=request.POST)
  if form.is_valid():
    user = form.get_user()
    django_login(request, user)
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    clear_temp()
    return HttpResponseRedirect(reverse('randomizer.views.index'))
  else:
    return {"auth_form": form}


@require_POST
def logout(request):
  if request.user.is_authenticated():
    django_logout(request)
  return HttpResponseRedirect(reverse('randomizer.views.index'))



@ensure_csrf_cookie
@render_to("update.html")
def update(request):
  return csrf(request)


@is_ajax
@require_POST
def get_update(request):
  return HttpResponse(loadConstelation())



@is_ajax
@require_POST
def submit(request):
  data = simplejson.loads(request.raw_post_data)
  if not "maxteams" in data and not "nations" in data:
    return HttpResponse("nothing to randomize!")
  nations = data.get("nations", [])
  maxteams = data.get("maxteams", 0)
  players = data.get("players", [])
  if not players:
    return HttpResponse("no players found!")

  saveConstelation(randomize(players, int(maxteams), nations))
  return HttpResponse("OK")