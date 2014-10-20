from django.db import models

class WifiInfo(models.Model):
	ssid = models.CharField(max_length = 200)
	pswd = models.CharField(max_length = 200)
