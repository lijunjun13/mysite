from django.shortcuts import render
from django.shortcuts import HttpResponse
# -*- coding: utf-8 -*-
import json
import sys
import logging
import pandas as pd
import numpy as np
# import pandas.Se
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY,HourLocator, MinuteLocator, SecondLocator, MonthLocator
import matplotlib.dates as mdate
import datetime
import pymysql as mdb
# import ConfigParser
# Create your views here.

# logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                         datefmt='%d %b %Y %H:%M:%S',
#                         args=(sys.stderr, ))
# try:
#     cf = ConfigParser.ConfigParser()
#     cf.read("../conf/database.conf")
# except:
#     logging.warning("unable to read config file!")

try:
    conn = mdb.connect(host="127.0.0.1", port=3306,
                       user="lijunjun", passwd="ljj3771thu",
                       db="stock", charset="utf8")
except:
    logging.warning("unable to connect database")

cursor = conn.cursor()
sql="SELECT * FROM cars;"
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)
user_list=[]
for row in rows:
    car_no = row[0]
    car_style = row[1]
    car_owner = row[2]
    car_capacity = row[3]
    car_routine = row[4]
    car_price = row[5]
    newitem = {"car_no":car_no,
               "car_style":car_style,
               "car_owner":car_owner,
               "car_capacity":car_capacity,
               "car_routine":car_routine,
               "car_price":car_price}
    user_list.append(newitem)


def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("hello world!")
    if request.method=="GET":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        temp = {"user":username, "pwd": password}
        user_list.append(temp)
        print(username, password)
    return render(request, "index.html", {"data":user_list})


def home(request):
    return render(request, 'home.html',{"data": user_list})


def detail(request):
    car_id = int(request.GET.get("id",0))
    if car_id == 0:
        return render(request, 'detail.html')
    else:
        data = user_list[car_id-1]
        return render(request, 'detail.html',{"data": data})


def graph(request):
    return render(request, 'graph2.html')