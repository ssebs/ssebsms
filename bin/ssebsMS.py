###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
# ssebsMS.py file structure:
#   1) [x] handle imports
#   2) [x] help output text
#   3) [x] main function
#   4) [ ] hande init
#   5) [ ] hande build
#   6) [ ] hande clean
#   7) [x] get arguments
#   8) [x] main func def
# have website be object oriented?
##

## 1 - handle imports ##
import os,sys
sys.dont_write_bytecode=True    # disable .pyc files

from markdown import markdown
from _init import init_test, init_entry
from _build import build_test
from _clean import clean_test

## 2 - help output below (future commands to support) ##
help_output = '''ssebsMS.py <CMD> <site-name>

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files
    help        <- output this help page
'''
## 3 - main function ##
def main(argv):
    cmd = ""    # Command to run

    #sample_md = '''# ssebs\n## Home page\nssebs home!\n'''
    #print(markdown(sample_md))

    # choose what to do next depending on arg
    cmd = get_args(argv)
    print(cmd)

    if "init" in cmd:
        print("Initializing ssebsMS website...")
        init(cmd[1])
        print("ssebsMS website initialized.")
    elif "build" in cmd:
        print("Building ssebsMS website...")
        build(cmd[1])
        print("ssebsMS website built.")
    elif "clean" in cmd:
        print("Cleaning ssebsMS website...")
        clean(cmd[1])
        print("ssebsMS website cleaned.")
    elif "debug" in cmd:
        pass
    else:
        print(help_output)
        exit(1)

# end main

## 4 - initialization of website data ##
def init(site_name):
    init_test("ssebs_init")
    init_entry(site_name)
    pass
# end init()

## 5 - build existing website content
def build(site_name):
    build_test("ssebs_build")
    pass
# end build()

# 6 - clean generated website
def clean(site_name):
    clean_test("ssebs_clean")
    pass
# end clean

## 7 - get args from cli ##
def get_args(argv):
    num_arg = len(sys.argv)
    cmd_arg = [None, None]

    if num_arg == 1:    # ssebsMS.py 
        return ""
    elif num_arg == 2:  # ssebsMS.py CMD
        cmd_arg = [sys.argv[1], "my_site"]
    elif num_arg == 3:  # ssebsMS.py CMD site-name
        cmd_arg = [sys.argv[1], sys.argv[2]]
    else:               # ssebsMS.py CMD site-name ??? ?? ?
        return ""
    return cmd_arg
# end get_args()

## 8 - main func def ##
if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)