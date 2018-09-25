###
#   ssebsMS.py - ssebsMS cli utility
###

##
# ssebsMS.py file structure:
#   - [x] main function
#   - [x] handle imports
#   - [x] help output text
#   - [x] get arguments
#   - [ ] handle each argument
#   - [x] main func def
# have website be object oriented?
##

## imports ##
import os,sys
from markdown import markdown

## help output below (future commands to support) ##
help_output = '''ssebsMS.py <CMD> 

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files
    help        <- output this help page
'''
## main function ##
def main(argv):
    cmd = ""    # Command to run
    sample_md = '''# ssebs\n## Home page\nssebs home!\n'''
    print(markdown(sample_md))

    # choose what to do next depending on arg
    cmd = get_args(argv)

    if "init" in cmd:
        print("Initializing ssebsMS website...")
        #initialize_cms()
        print("ssebsMS website initialized.")
    elif "build" in cmd:
        print("Building ssebsMS website...")
        #build_cms()
        print("ssebsMS website built.")
    elif "clean" in cmd:
        print("Cleaning ssebsMS website...")
        #clean_cms()
        print("ssebsMS website cleaned.")
    elif "debug" in cmd:
        pass
    else:
        print(help_output)
        exit(1)

# end main

## get args from cli ##
def get_args(argv):
    num_arg = len(sys.argv)
    cmd_arg = None

    if num_arg == 1:    # ssebsMS.py 
        return ""
    elif num_arg == 2:  # ssebsMS.py CMD
        cmd_arg = sys.argv[1]
    else:               # ssebsMS.py CMD ??? ?? ? 
        return ""
    return cmd_arg
# end get_args()

## main func def ##
if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)