# -*- coding: UTF-8 -*- 
from django.http import HttpResponse # for DEBUG, print simple http response
#template
from django.shortcuts import render_to_response
from django.template import RequestContext
#json
import json

from models import WifiInfo

def list(request):
	all_wifi = WifiInfo.objects.all()
	return render_to_response('list.html', locals(), context_instance=RequestContext(request))

#set ssid and password
def set(request):
	errors = []
	if request.method == "GET":
		if not request.GET.get('ssid', ''):
			errors.append('ssid missing')
		if not request.GET.get('pswd', ''):
			errors.append('pswd missing')
		if not errors:
			ssid = request.GET['ssid']
			pswd = request.GET['pswd']
			wifi = WifiInfo(ssid=ssid, pswd=pswd)
			wifi.save()
			return  HttpResponse('Success')
	return HttpResponse('Error')

#get ssid and password
def get(request):
	errors = []
	response_data = {}
	if request.method == "GET":
		if not request.GET.get('ssid', ''):
			errors.append('ssid missing')
		if not errors:
			ssid = request.GET['ssid']
			try:
				wifi = WifiInfo.objects.get(ssid=ssid)
				response_data['pswd'] = wifi.pswd
			except:
				errors.append('ssid wrong')
		else:
			response_data['error'] = 'error'
	if not errors:
		return HttpResponse(response_data['pswd'])
	else:
		return HttpResponse('')
	#return HttpResponse(json.dumps(response_data), content_type="application/json")