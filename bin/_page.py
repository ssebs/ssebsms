###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
##

##
#   This file should contain a class definition for a 'page' object
##

from markdown import markdown

class Page:
    def __init__(self, site_name, url, filename, header_file, footer_file):
        """
        ;:param site_name:
        :param url:
        :param filename:
        :param header_file:
        :param footer_file:
        """
        # param based attrs
        self.site_name = site_name
        self.url = url
        self.filename = filename
        self.header_file = header_file
        self.footer_file = footer_file

        # empty vars to be filled from files
        self.title = ""
        self.url = ""
        self.author = ""

        # built attrs
        self.page_txt = self.get_page_text()
        self.header_txt = self.get_header_text()
        self.footer_txt = self.get_footer_text()

        self.raw_sections = self.get_sections() # self.raw_sections now contains list of sections w/ data
        self.sections = self.process_sections() # process the above var to parse important data / get ready to convert

    # end constructor


    def get_page_text(self):
        with open(self.filename) as f:
            return f.readlines()
    # end print_page

    def get_header_text(self):
        with open(self.header_file) as f:
            return f.readlines()
    # end print_header

    def get_footer_text(self):
        with open(self.footer_file) as f:
            return f.readlines()
    # end print_header

    def get_sections(self):
        """

        :returns: list of sections, with content of section in each part
        """
        ## mdx syntax below
        # !~title=<PAGE_TITLE>
        # !~url=<URL.html>
        # !~author=<YOUR NAME>
        #
        # ~start-section=<SECTION_NAME>  # COMMENT
        # ~sec-theme=<THEME OF SECTION>  # COMMENT
        # ~sec-option=<sec-theme OPTION> # COMMENT
        #
        # <YOUR MARKDOWN HERE>
        #
        # ~end-section=<SECTION_NAME>
        #
        # <OPTIONAL SECTION2 USING SAME SYNTAX ABOVE>
        #
        ##
        ret = []        # final return list
        tmp_str = ""    # tmp string to hold section data
        start_sec = False
        for line in self.page_txt:
            # set top config vars
            if line.startswith("!~title="):
                self.title = line.split("=")[1].strip("\n").strip()
                #print("Title = " + self.title)
            elif line.startswith("!~url"):
                self.url = line.split("=")[1].strip("\n").strip()
                #print("URL = " + self.url)
            elif line.startswith("!~author"):
                self.author = line.split("=")[1].strip("\n").strip()
                #print("Author = " + self.author)

            # get sections
            if line.startswith("~start-section="):
                start_sec = True
            elif line.startswith("~end-section="):
                start_sec = False
                ret.append(tmp_str)
                tmp_str = ""
            if start_sec:
                #if line != "\n":
                    #tmp_str += line
                tmp_str += line
            else:
                pass
        # end for-line
        return ret
    # end get_sections

    def process_sections(self):
        """

        :returns parsed mdx sections
        """
        pass

    # end process_sections()

    ## Main rendering method
    def render_page(self):
        tmp = ""
        for line in self.header_txt:
            tmp += line
        print(markdown(tmp))
        pass
    # end render_page
# end class Page

## TEST ##
p = Page("test", "index.html",
         "./test/pages/home/home.mdx",
         "./test/page-parts/header.md",
         "./test/page-parts/footer.md")

#print("Printing header:")
#print(p.get_header_text())

#print("Rendering:")
#p.render_page()
#print("Page txt below")
#print(p.get_page_text())

print("Sections below")

for s in p.raw_sections:
    print("SECTION: \n" + s)
