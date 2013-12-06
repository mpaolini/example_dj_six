from django.shortcuts import render_to_response
from django.template import RequestContext

import time, random

def home(request, template_name="home.html"):

	millis = int(round(time.time() * 1000))
	random.seed(millis)
	data = {'userno': random.randint(1,90)}
	return render_to_response(template_name, data, context_instance=RequestContext(request))