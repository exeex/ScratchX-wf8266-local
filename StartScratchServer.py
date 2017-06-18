#!/usr/bin/env python

import http.server
import webbrowser
import socket
import urllib.request


def get_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "127.0.0.1"
    return ip


def run_server(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("running scratch...")
    ip = get_ip()
    webbrowser.open("http://" + ip + ":8000", new=0, autoraise=True)
    httpd.serve_forever()


if __name__ == "__main__":

    # 取得本機ip
    ip = get_ip()
    url = "http://{}:8000".format(ip)

    # 嘗試連線，若無法連線則開啟網頁伺服器
    try:
        ret = urllib.request.urlopen(url)

    except (urllib.error.URLError, ConnectionRefusedError):
        Handler = http.server.SimpleHTTPRequestHandler
        run_server(server_class=http.server.HTTPServer, handler_class=Handler)

    # 開啟瀏覽器
    webbrowser.open(url, new=0, autoraise=True)
