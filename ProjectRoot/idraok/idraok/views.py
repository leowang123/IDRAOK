from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def home(request):
	#item = 'img/background.jpg'
	t = get_template('Front_page.html')
	html = t.render(Context())
	return HttpResponse(html)
