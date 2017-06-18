#!/usr/bin/env python
 
import http.server
import webbrowser
import socket
import urllib.request
import queue

Handler = http.server.SimpleHTTPRequestHandler

def run_server(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("running scratch...")
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "127.0.0.1"
    webbrowser.open("http://"+ip+":8000", new=0, autoraise=True)
    httpd.serve_forever()

try:
    ip = socket.gethostbyname(socket.gethostname())
except:
    ip = "127.0.0.1"

url = "http://{}:8000".format(ip)

try:
    ret = urllib.request.urlopen(url)
except:
    ret = 0

if ret != 0 & ret.status == 200:
    webbrowser.open(url, new=0, autoraise=True)
else:
    run_server(server_class = http.server.HTTPServer, handler_class = Handler)
