from misc.decorator import render_to, is_ajax
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf
from django.views.decorators.http import require_POST

from django.utils import simplejson

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
  return output



@ensure_csrf_cookie
@render_to("update.html")
def update(request):
  return csrf(request)


@is_ajax
@require_POST
def get_update(request):
  return HttpResponse("OK")

from randomizer import randomize
import traceback


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
  try:
    randomize(players, int(maxteams), nations)
  except Exception, e:
    traceback.print_exc(e)
    raise e

  return HttpResponse("OK")