###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
##

## Procedure on how pages will be built:
# 0) [ ] Check / read config file
# 1) [ ] list dirs
# 2) [ ] check for md files & make sure they match config
# 3) [ ] loop through page md files and get file based configs
#   4) [ ] make list of page objects & set their settings
#   5) [ ] read contents of Markdown
#   6) [ ] generate html per page in public/ dir
# 7) Test to make sure pages are there


# test definition for import testing
def build_test(my_arg):
    print("I'm in the _init.py file! Even " + str(my_arg) + " is here!")