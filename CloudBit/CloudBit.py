#!/usr/bin/python3
import http.server
import socketserver
import sys
import os
import threading
from urllib.parse import quote
import psutil
import qrcode


def get_netcard():  
    netcard_info = []  
    info = psutil.net_if_addrs()  
    for k,v in info.items():  
        for item in v:  
            if item[0] == 2 and not item[1] == '127.0.0.1':  
                netcard_info.append((k,item[1]))  
    return netcard_info


def url_to_qrcode(url):
    text = qrcode.make(url)
    text.show()


def http_server(port):
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('', port), Handler)
    print("serving at port", port)
    httpd.serve_forever()


def choose_networkcard():
    netcard_info = get_netcard()
    netcard_info_line = ''
    for i,v in enumerate(netcard_info):
        netcard_info_line += '[{}]:'.format(i)
        netcard_info_line += 'name: ' + v[0]
        netcard_info_line += '  ip: ' + v[1]
        netcard_info_line += '\n'
    print('usually the network ip startswith 192.168')
    choice = input(netcard_info_line)
    try:
        choice = int(choice)
    except ValueError as e:
        print('wrong choice,exit now')
        
        os._exit(1)
    else:
        if isinstance(choice,int) and choice <= len(netcard_info):
            ip = netcard_info[choice][1]
            return ip
        else:
            print('wrong choice,exit now')
            os._exit(1)


if __name__ == '__main__':
    port = 8002
    t = threading.Thread(target=http_server,args=(port,))
    t.start()
    if len(sys.argv) > 1:
        print('to many args...')
        os._exit(1)
    file_path = 'C:\\'
    ip = choose_networkcard()
    url = f'http://{ip}:{port}/' #+ quote(file_path)
    url_to_qrcode(url)