#!/usr/bin/env python
 
import http.server
import webbrowser
import socket
import requests
import queue

Handler = http.server.SimpleHTTPRequestHandler

def run_server(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("running scratch...")

    ip = socket.gethostbyname(socket.gethostname())
    webbrowser.open("http://"+ip+":8000", new=0, autoraise=True)
    httpd.serve_forever()


ip = socket.gethostbyname(socket.gethostname())
url = "http://{}:8000".format(ip)
try:
    ret = requests.get(url)
except:
    ret = None

if ret != None:
    webbrowser.open(url, new=0, autoraise=True)
else:
    run_server(server_class = http.server.HTTPServer, handler_class = Handler)