###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
##

## _build.py file structure
# 1) imports
# 2) variable defs
# 3)
# 4) entry

## Procedure on how pages will be built ##
# [x] Check / read config file
# [x] list dirs / get from conf...
# [ ] check for md files & make sure they match config
# [ ] loop through page md files and get file based configs
#   [ ] make list of page objects & set their settings
#   [ ] read contents of Markdown
#   [ ] generate html per page in public/ dir
# [ ] test to make sure pages are there

# 1 - imports
import os,yaml

# 2 - variable defs
site_config = {}  # dictionary containing site config data (pages,page files, etc)
pages_list = []   # list of the pages to render (home/about/etc)
pages = []

# 3 -

# entry of build module
def build_entry(site_name):
    if site_name in os.listdir("./"):

        # read site config from sitename/conf.yml
        site_config = yaml.load(open(site_name + "/conf.yml"))
        #print("Site config: \n" + str(site_config))
        site_config = site_config[0] # load() creates a list of 1 dict...

        # get list of pages from conf
        lenvar = len(site_config['pages'])
        for x in range(0,lenvar):
            for k, v in site_config['pages'][x].items():
                pages_list.append(k)

        # check for md files in each page's directory just in case
        for p in pages_list:
            print(os.listdir(site_name + "/pages/" + p + "/"))
            # TODO: Create object based on page config
            # p = (home|about)
            # filename param has to be full rel path e.g. site_name/pages/$p/$p['filename']
            # pages.append(Page("url","filename","header_file","footer_file"))
    else:
        #print("ls: " + str(os.listdir("./")))
        print("No " + site_name + "/ directory found. Have you run 'ssebsMS.sh init'? See help...")
# end entry()

# test definition for import testing
def build_test(my_arg):
    print("I'm in the _build.py file! Even " + str(my_arg) + " is here!")