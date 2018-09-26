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

        :param url:
        :param filename:
        :param header_file:
        :param footer_file:
        """
        # param based attrs
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

        self.sections = self.get_sections()

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
        ret = []
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


        return ret
    # end get_sections

    ## Main rendering method
    def render_page(self):
        print(markdown(self.header_txt))
        #print(markdown(self.page_txt))
        #print(markdown(self.footer_txt))
        pass
    # end render_page
# end class Page

## TEST ##
p = Page("test",
        "index.html", "./test/pages/home/home.mdx",
         "./test/page-parts/header.md",
         "./test/page-parts/footer.md")

#print("Printing header:")
#print(p.get_header_text())

#print("Rendering:")
#p.render_page()
#print("Page txt below")
#print(p.get_page_text())

print("Sections below")
print(p.sections)