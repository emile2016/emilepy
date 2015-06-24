# -*- coding: utf-8 -*-
from django.http import HttpResponse
import django
def home(request):
	return HttpResponse('Django Version = ' + str(django.VERSION), mimetype="text/plain")