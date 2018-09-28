###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
##

import http.server
import socketserver
import os


def srv(site_name,port):
    os.chdir("./" + site_name + "/public/")

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print("Serving at http://localhost:{}".format(port))
    httpd.serve_forever()
# end srv()


def run_entry(site_name="test",port=8008):
    srv(site_name,port)
# end run_entry()
