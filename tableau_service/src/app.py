
from http.server import BaseHTTPRequestHandler,HTTPServer
import http.server
import socketserver
import os
from display import DISPLAY



class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if os.environ.get('DISPLAY','') == '':
            os.environ.__setitem__('DISPLAY', DISPLAY)
        
        os.system("firefox https://sso.online.tableau.com/public/idp/SSO")


# Here we define that we want to start the server on port 1234. 
# Try to remember this information it will be very useful to us later with docker-compose.
with socketserver.TCPServer(("", 3010), MyHandler) as httpd:
    # This instruction will keep the server running, waiting for requests from the client.
    httpd.serve_forever()