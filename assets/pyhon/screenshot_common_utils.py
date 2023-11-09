import os
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import win32com.client
from assets.pyhon.webdriver_setup import initialize_webdriver
from assets.pyhon.screenshot_common_save import configure_webpage