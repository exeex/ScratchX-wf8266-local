#!/usr/bin/env python

import http.server
import webbrowser
import socket
import urllib.request
import urllib.error
from multiprocessing import Process
import time

import tkinter as tk
import os


def get_ip():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "127.0.0.1"
    return ip


def get_url():
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = "127.0.0.1"

    url = "http://{}:8000".format(ip)
    return url


def run_server():
    ip = get_ip()
    url = "http://{}:8000".format(ip)

    try:
        ret = urllib.request.urlopen(url)

    except (urllib.error.URLError, ConnectionRefusedError):
        handler = http.server.SimpleHTTPRequestHandler
        server_address = ('', 8000)
        httpd = http.server.HTTPServer(server_address, handler)
        httpd.serve_forever()



def open_web():
    url = get_url()
    webbrowser.open(url, new=0, autoraise=True)
    return

def open_win():
    # 啟動視窗
    win = tk.Tk()
    win.title("ScratchX單機版")
    win.minsize(width="150",height="50")
    label = tk.Label(win, text="ScratchX")  # 建立標籤物件
    label.grid(columnspan=6)  # 顯示元件
    button = tk.Button(win, text="開啟ScratchX", command=open_web)
    button.grid(row=1, column=0, columnspan=4)  # 顯示元件
    button = tk.Button(win, text="關閉", command=win.destroy)
    button.grid(row=1, column=10, columnspan=4)  # 顯示元件
    win.mainloop()

if __name__ == "__main__":
    # 取得本機ip
    ip = get_ip()
    url = get_url()

    # 嘗試連線，若無法連線則開啟網頁伺服器



    try:
        ret =  urllib.request.urlopen(url)
        open_web()

    except (urllib.error.URLError, ConnectionRefusedError):
        p = Process(target=run_server)
        p.start()
        print("running scratch...")
        open_win()
        p.terminate()
