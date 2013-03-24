#!/usr/bin/python

import socket
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

url = socket.gethostbyname(socket.gethostname()) + ":8000"
print "Open this in your smartphone on the same local network: " + "http://" + url

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = [""]

httpd = server(server_address, handler)
httpd.serve_forever()