###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
# ssebsMS.py file structure:
#   1) [x] handle imports
#   2) [x] help output text
#   3) [x] main function
#   4) [x] handle init
#   5) [ ] handle build
#   6) [x] handle clean
#   7) [x] get arguments
#   8) [x] main func def
# have website be object oriented?
##

## 1 - handle imports ##
import os,sys
sys.dont_write_bytecode=True    # disable .pyc files

from markdown import markdown
from _init import init_test, init_entry
from _build import build_test, build_entry
from _clean import clean_test, clean_entry

## 2 - help output below (future commands to support) ##
env_filename = "ENV-ssebsMS"
help_output = '''ssebsMS.sh <CMD> [site-name]

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files (delete for now)
    help        <- output this help page

ENV file:
    ''' + env_filename + '''    <- Modify this file so you don't have to 
specify [site-name] in every command.
'''
## 3 - main function ##
def main(argv):
    cmd = ""    # Command to run

    # choose what to do next depending on arg
    cmd = get_args(argv)

    if "init" in cmd:
        print("Initializing " + cmd[1] + "website...")
        init(cmd[1])
        print(cmd[1] + " website initialized.")
    elif "build" in cmd:
        print("Building " + cmd[1] + " website...")
        build(cmd[1])
        print(cmd[1] + " website built.")
    elif "clean" in cmd:
        print("Cleaning " + cmd[1] + " website...")
        clean(cmd[1])
        # TODO: have a clean and a delete
        print(cmd[1] + " website cleaned.")
    elif "debug" in cmd:
        print("Args: " + str(cmd) + "\n\n")
        sample_md = '''
# ssebs
<hr>
## Home page

ssebs home!
        '''
        print(markdown(sample_md))
    else:
        print(help_output)
        exit(1)

# end main

## 4 - initialization of website data ##
def init(site_name):
    #init_test("ssebs_init")
    init_entry(site_name, env_filename)
    pass
# end init()

## 5 - build existing website content
def build(site_name):
    #build_test("ssebs_build")
    build_entry(site_name)
    pass
# end build()

# 6 - clean generated website
def clean(site_name):
    #clean_test("ssebs_clean")
    clean_entry(site_name, env_filename)
    pass
# end clean

## 7 - get args from cli ##
def get_args(argv):
    num_arg = len(sys.argv)
    cmd_arg = [None, None]

    if num_arg == 1:    # ssebsMS.py 
        return ""
    elif num_arg == 2:  # ssebsMS.py CMD
        # check local environment file
        if env_filename in os.listdir("./"):
            with open(env_filename, "r") as f:
                #print("Contents of " + env_filename + ":")
                for l in f:
                    if not l.startswith("#"):
                        #print("config line: " + l.strip("\n"))
                        if l.startswith("site-name"):
                            tmp = l.split("=")[1].strip()
                            print("site-name is: " + tmp + ". To change this, delete the line in " + env_filename + " or run with <sitename> parameter.\n")
                            cmd_arg = [sys.argv[1], tmp]
                    else:
                        # line in file starts with a comment
                        pass
            # end with open
        else:
            ans = input("Are you sure you want to use the default site at 'my_site/'? ")
            if 'y' in ans.lower():
                cmd_arg = [sys.argv[1], "my_site"]
            else:
                print("Please add a site name to the end of your command. e.g. 'ssebsMS.py CMD site-name'\n")
                return ""
    elif num_arg == 3:  # ssebsMS.py CMD site-name
        cmd_arg = [sys.argv[1], sys.argv[2]]
    else:               # ssebsMS.py CMD site-name ??? ?? ?
        return ""
    return cmd_arg
# end get_args()

## 8 - main func def ##
if __name__ == "__main__":
    main(sys.argv)
