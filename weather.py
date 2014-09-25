#! /usr/bin/env python
# coding:utf-8
import requests
import os

location = 'Sapporo'

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + ',jp')
os.system("echo "+r.json()["weather"][0]["description"]+" "+str(int(r.json()["main"]["temp"])-273.0))
