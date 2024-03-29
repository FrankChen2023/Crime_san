import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from crime_main import app

CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--proxy-server='direct://")
chrome_options.add_argument("--proxy-bypass-list=*")

def before_all(context):
    context.sever = simple_server.WSGIServer(("", 2500), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
    context.browser.set_page_load_timeout(time_to_wait=200)

def after_all(context):
    context.browser.quit()
    context.sever.shutdown()
    context.pa_app.join()
    