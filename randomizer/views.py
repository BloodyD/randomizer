from misc.decorator import render_to

from randomizer.forms import MainForm
from randomizer import *

@render_to("index.html")
def index(request):
  return {
  "names": NAMES[:2],
  "not_in_game": NAMES[2:],
  "nations":NATIONS}