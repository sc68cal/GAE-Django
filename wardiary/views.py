# Create your views here.
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from models import WarDiary
from django.template import Context, loader
from django.http import HttpResponse
from google.appengine.ext import db

def report_detail(request,object_id):
	query = db.get(db.Key(object_id))
	t = loader.get_template('wardiary/wardiary_detail.html')
	c = Context({"object":query})
	return HttpResponse(t.render(c))


def report_list(request):
	query = WarDiary.all().fetch(1000)
	t = loader.get_template("wardiary/wardiary_list.html")
	c = Context({"object_list":query})
	return HttpResponse(t.render(c))
