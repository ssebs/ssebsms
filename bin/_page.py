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
    def __init__(self, url, filename, header_file, footer_file):
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

        # built attrs
        self.page_txt = self.get_page_text()
        self.header_txt = self.get_header_text()
        self.footer_txt = self.get_footer_text()

    # end constructor


    def get_page_text(self):
        with open(self.filename) as f:
            return f.read()
    # end print_page

    def get_header_text(self):
        with open(self.header_file) as f:
            return f.read()
    # end print_header

    def get_footer_text(self):
        with open(self.footer_file) as f:
            return f.read()
    # end print_header

    ## Main rendering method
    def render_page(self):
        print(markdown(self.header_txt))
        #print(markdown(self.page_txt))
        #print(markdown(self.footer_txt))
        pass
    # end render_page
# end class Page

## TEST ##
p = Page("index.html", "./test/pages/home/home.md",
         "./test/page-parts/header.md",
         "./test/page-parts/footer.md")

print("Printing header:")
print(p.get_header_text())

print("Rendering:")
p.render_page()