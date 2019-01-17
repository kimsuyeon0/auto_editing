from bs4 import BeautifulSoup 
import lxml 
import requests
import math
import os
import time
import csv
import calendar
import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from urllib.request import urlopen
import lxml
import requests
from selenium.webdriver.common.keys import Keys 
import datetime
from pytube import YouTube
import urllib.request




# urllib.request.urlretrieve(url_link, video_name.mp4)
# 다른 사이트에서 링크 받은 걸 넣으면 mp4파일로 만들어 준다.

main_url = "https://www.youtube.com/channel/UCFyiXkln3xqNiW4JL912FLA/videos"
driver = webdriver.Chrome("C:/driver_craw/chromedriver.exe")
driver.get(main_url)
time.sleep(3)


