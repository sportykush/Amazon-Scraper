# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:59:05 2019

@author: sportykush
"""
 
import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/Mivi-Moonstone-Portable-Wireless-Output-Black/dp/B07J4T9LZG/ref=sr_1_2?keywords=mivi+speakers&qid=1568106165&s=gateway&sr=8-2'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content , 'html.parser')
    #title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])
    if(converted_price < 1.400):
        send_mail()
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('-your email id-', '-your password-')
    subject = "buy speakers"
    body = 'Check the speaker link https://www.amazon.in/Mivi-Moonstone-Portable-Wireless-Output-Black/dp/B07J4T9LZG/ref=sr_1_2?keywords=mivi+speakers&qid=1568106165&s=gateway&sr=8-2'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
            '-your email id-',
            '-recievers email id-',
            msg
        )
    print('Mail sent')
    server.quit()
    
while(True):
    check_price()
    time.sleep(60*60*24)
        
