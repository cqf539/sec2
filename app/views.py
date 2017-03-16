from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import datetime


# Create your views here.
def hello(req):
    return HttpResponse("hello world")

def current_datetime(req):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(req, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)