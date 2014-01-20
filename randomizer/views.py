from misc.decorator import render_to

@render_to("index.html")
def index(request):
  return {}