# run.py - run simplehttp server for website.

import http.server
import socketserver
import os

PORT = 8008
site_name = "test"

web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir("./" + site_name + "/public/")

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("Serving at http://localhost:{}".format(PORT))
httpd.serve_forever()