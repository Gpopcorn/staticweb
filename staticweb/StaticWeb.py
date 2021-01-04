import socket
import sys
import os

class WebServer:
    path_templates = []
    path_urls = []

    def __init__(self, ip, port):
        self.page404 = ''

        self.ip = ip
        self.port = port

    def Set404Page(self, page):
        self.page404 = page

    def SetPath(self, template, url):
        self.path_urls.append(url)
        self.path_templates.append(template)

    def MainLoop(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.ip, self.port))
        s.listen(1)
        print(f'[LISTENING] Now listening on address: {self.ip}:{self.port}')

        while True:
            try:
                cs, addr = s.accept()
                request = cs.recv(1024).decode()

                headers = request.split('\n')
                try:
                    url = headers[0].split()[1]
                except IndexError:
                    continue

                try:
                    if any(url in s for s in self.path_urls):
                        templatenumber = self.path_urls.index(url)
                        htmlfile = open(self.path_templates[templatenumber])
                    else:
                        htmlfile = open('templates' + url)

                    htmlcontent = htmlfile.read()
                    htmlfile.close()

                    response = f'HTTP/1.0 200 OK\n\n{htmlcontent}'
                    print(f'[CONNECTION] Connection at url: {url}')
                except FileNotFoundError:
                    if self.page404 == '':
                        response = 'HTTP/1.0 404 NOT FOUND\n\n<h1>404 Page Not Found!</h1>'
                    else:
                        try:
                            page404file = open('error-templates/' + self.page404)
                            page404content = page404file.read()
                            page404file.close()
                            response = f'HTTP/1.0 404 NOT FOUND\n\n{page404content}'
                        except FileNotFoundError:
                            response = 'HTTP/1.0 404 NOT FOUND\n\n<h1>404 Page Not Found</h1>'
                    print(f'[404 ERROR] 404 error at url: {url}')
                
                cs.sendall(response.encode())
                cs.close()
            except KeyboardInterrupt:
                print('[INTERRUPT] Program Interrupted')
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)

        s.close()

def LocalHost():
    return '0.0.0.0'
