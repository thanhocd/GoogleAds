from selenium import webdriver
import requests
import time
import random


class BeeHelper:

    def push_everything (self, url ,data ):
       
        # try de co bi loi cung ko lam gian doan function chinh 
        try:
            payload={ 'data': str(data) }
            response = requests.request("POST", url, data=payload)
            return response 
        except Exception as e: # de loi j no con log ra 
            print(str(e))


def test_module  ():
    print('Hello World')

#test_module()