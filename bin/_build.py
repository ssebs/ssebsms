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
# [x] check for mdx files from config
# [x] loop through page md files and get file based configs (Done in _page.py)
#   [x] make list of page objects & set their settings
#   [ ] read contents of Markdown
#   [ ] generate html per page in public/ dir
# [ ] test to make sure pages are there

# 1 - imports
import os, yaml, json


# 2 - variable defs
site_config = {}    # dictionary containing site config data (pages,page files, etc)
pages_list = []     # list of the pages to render (home/about/etc)
pages = []          # list of page objects

# 3 -

# entry of build module
def build_entry(site_name):
    from _page import Page  # needs to be imported here or else it doesn't contruct properly
    if site_name in os.listdir("./"):

        # read site config from sitename/conf.yml
        site_config = yaml.load(open(site_name + "/conf.yml"))
        # print("Site config: \n" + json.dumps(site_config))

        # get list of pages from conf
        lenvar = len(site_config['pages'])
        for x in range(0, lenvar):
            for k, v in site_config['pages'][x].items():
                pages_list.append(k)

        # create page objects for pages found from config
        for count, page_name in enumerate(pages_list):
            #print("Page " + page_name)
            for k, v in site_config['pages'][count - 1].items():
                # print("Page: " + k + " file:" + v['filename'])
                # print("Page: " + k + " hdr:" + v['header'])
                # print("Page: " + k + " ftr:" + v['footer'])
                pages.append(Page(site_name, (k + "/" + v['filename']), v['header'], v['footer']))

        # render pages to html, and write to public/ dir
        for page in pages:
            print("Printing page: " + page.title)
            print(page.render_page()[0])

    else:
        # print("ls: " + str(os.listdir("./")))
        print("No " + site_name + "/ directory found. Have you run 'ssebsMS.sh init'? See help...")
# end entry()

# test definition for import testing
def build_test(my_arg):
    print("I'm in the _build.py file! Even " + str(my_arg) + " is here!")
