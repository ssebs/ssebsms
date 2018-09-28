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
import os, yaml, shutil


# 2 - variable defs
site_config = {}    # dictionary containing site config data (pages,page files, etc)
pages_list = []     # list of the pages to render (home/about/etc)
pages = []          # list of page objects


# generate ToC
def gen_ToC():
    #print("Generating Table of Contents...")
    ##
    #   Goal: make list (html) of pages using the page obj's url
    ##
    ret = '''
\t<nav>
\t\t<ul style="list-style-type: none;">
'''

    # TODO: Figure out how to make this ordered without hard coding home
    for p in pages:
        if "home" in p.page_dir.lower():
            ret += '\t\t\t<li style="display: inline-block;"><a href="./' + p.url + '">' + p.page_dir.capitalize() + '</a></li>\n'

    for p in pages:
        #print(p.page_dir + ", " + p.url)
        if "home" not in p.page_dir.lower():
            ret += '\t\t\t<li style="display: inline-block;"><a href="./' + p.url + '">' + p.page_dir.capitalize() + '</a></li>\n'
    ret += '''\t\t</ul>
\t</nav>
'''
    # print("ToC: \n" + ret)
    return ret
# end get_ToC()

# entry of build module
def build_entry(site_name):
    from _page import Page  # needs to be imported here or else it doesn't construct properly
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
            # print("Page " + page_name)
            for k, v in site_config['pages'][count - 1].items():
                # print("Page: " + k + " file:" + v['filename'])
                # print("Page: " + k + " hdr:" + v['header'])
                # print("Page: " + k + " ftr:" + v['footer'])
                pages.append(Page(site_name, k, v['filename'], v['header'], v['footer']))

        # render pages to html, and write to public/ dir
        for page in pages:
            print("Generating page: " + page.title + " at: " + site_name + "/public/" + page.url)
            # print("url:" + page.url)
            # print(page.render_page()[0])

            # render pages to site_name/public/ folder
            with open(site_name + "/public/" + page.url, "w") as f:
                f.write(page.render_page(gen_ToC())[0])

            # copy images from pages/
            files = os.listdir(site_name + "/pages/" + page.page_dir + "/img/")
            for f in files:
                shutil.copy(site_name + "/pages/" + page.page_dir + "/img/" + f, site_name + "/public/img/")

            # copy styles from pages/
            files = os.listdir(site_name + "/pages/" + page.page_dir + "/style/")
            for f in files:
                shutil.copy(site_name + "/pages/" + page.page_dir + "/style/" + f, site_name + "/public/style/")

            # copy images from page-parts/
            files = os.listdir(site_name + "/page-parts/img/")
            for f in files:
                shutil.copy(site_name + "/page-parts/img/" + f, site_name + "/public/img/")

            # copy styles from page-parts/
            files = os.listdir(site_name + "/page-parts/style/")
            for f in files:
                shutil.copy(site_name + "/page-parts/style/" + f, site_name + "/public/style/")

    else:
        # print("ls: " + str(os.listdir("./")))
        print("No " + site_name + "/ directory found. Have you run 'ssebsMS.sh init'? See help...")
# end entry()

# test definition for import testing
def build_test(my_arg):
    print("I'm in the _build.py file! Even " + str(my_arg) + " is here!")
