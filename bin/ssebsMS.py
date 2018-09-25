###
#   ssebsMS.py - ssebsMS cli utility
###

##
# ssebsMS.py file structure:
#   - [x] handle imports
#   - [x] help output text
#   - [x] get arguments
#   - [ ] handle each argument
# have website be object oriented?
##

## imports ##
import os,sys

## help output below (future commands to support) ##
help_output = '''ssebsMS.py <CMD> 

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files
    help        <- output this help page
'''

## get the arguments from the user ##
num_arg = len(sys.argv)
cmd_arg = None

# check if they put an argument in at all, then set vars
if num_arg == 1:
    print(help_output)
    exit(1)
elif num_arg == 2:  # ssebsMS.py CMD
    cmd_arg = sys.argv[1]
else:
    print(help_output)
    exit(1)

# choose what to do next if they do have an argument
if "init" in cmd_arg:
    print("Initializing ssebsMS website...")
    #initialize_cms()
elif "build" in cmd_arg:
    print("Building ssebsMS website...")
    #build_cms()
elif "clean" in cmd_arg:
    print("Cleaning ssebsMS website...")
    #clean_cms()
else:
    print(help_output)
    exit(1)
