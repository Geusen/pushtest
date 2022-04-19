import settings
import tweepy
import shutil
import os
import time
import requests
import cv2 
import numpy as np
import pprint
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-----------------------------------------------------------------------------
#Googleにログイン
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#画像取得
file_id = drive.ListFile({'q': 'title = "upload.png"'}).GetList()[0]['id']
f = drive.CreateFile({'id': file_id})
f.GetContentFile('upload.png')
#----------------------------------------------------------------------------
