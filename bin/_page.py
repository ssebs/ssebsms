###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
#   This file should contain a class definition for a 'Page' object
#   'Page' object includes the following attributes after it's contructed
#   - site_name
#   - url
#   - filename
#   - header_file
#   - footer_file
#   - title
#   -
##

from markdown import markdown


class Page:
    def __init__(self, site_name, filename, header_file, footer_file):
        """
        :param site_name:
        :param filename:
        :param header_file:
        :param footer_file:
        """
        # param based attrs
        self.site_name = site_name
        self.filename = "./" + site_name + "/pages/" + filename
        self.header_file = "./" + site_name + "/page-parts/" + header_file
        self.footer_file = "./" + site_name + "/page-parts/" + footer_file

        # print(self.filename)
        # print(self.header_file)
        # print(self.footer_file)

        # empty vars to be filled from files
        self.title = ""
        self.url = ""
        self.author = ""

        # built attrs
        self.page_txt = self.get_page_text()        # pre-parsed txt. Final is in self.sections
        self.header_txt = self.get_header_text()    # final txt
        self.footer_txt = self.get_footer_text()    # final txt

        # raw_sections should be a list of text from mdx file, split by section
        # sections should be a list of parsed sections
        self.raw_sections = self.get_sections() # self.raw_sections now contains list of sections w/ data
        self.sections = self.process_sections() # process the above var to parse important data / get ready to convert

    # end constructor


    def get_page_text(self):
        with open(self.filename) as f:
            return f.readlines()
    # end print_page

    def get_header_text(self):
        with open(self.header_file) as f:
            #return f.readlines()
            return f.read()
    # end print_header

    def get_footer_text(self):
        with open(self.footer_file) as f:
            #return f.readlines()
            return f.read()
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
        ret = []  # list of section dictionaries [{}]
        sec_name = ""
        sec_theme = ""
        sec_option = ""
        sec_content = ""
        for c, sec in enumerate(self.raw_sections):
            # print("SECTION " + str(c+1))
            for line in sec.split("\n"):

                # get section name
                if line.startswith("~start-section="):
                    sec_name = line.split("=")[1].strip("\n").strip()

                # get section theme
                elif line.startswith("~sec-theme="):
                    sec_theme = line.split("=")[1]  # "parallax" # options available: parallax, billboard, color, blank
                    if "#" in sec_theme:
                        sec_theme = sec_theme.split("#")[0] # "parallax"
                    if "\"" in sec_theme:
                        sec_theme = sec_theme.replace("\"", "")
                    # print("Sec theme=" + sec_theme)

                # get section theme
                elif line.startswith("~sec-option="):
                    sec_option = line.split("=")[1] # "#41afff"  # options available: "img name", "color"
                    if "#" in sec_option:
                        # don't lose the hex color, but lose the possible comment after
                        if "#" in sec_option[:3]:   # maybe if the '#' is within 3 chars of the = it should be okay
                            # print(sec_option[:3])  # "#4
                            sec_option = sec_option.split("#")[1]  # "41afff"
                            sec_option = "#" + sec_option   # Add the '#' back for the hex color
                        else:   # value we want DOESN'T have '#' for hex code
                            sec_option = sec_option.split("#")[0]  # "code.jpg"
                    if "\"" in sec_option:
                        sec_option = sec_option.replace("\"", "")
                    # print("Sec opt=" + sec_option)
                # get section content
                else:
                    sec_content += (line + "\n").replace("\"", r'\"')    # Add the newline back
                # print("Line: " + line)

            # end line in section data

            # add new data to return list
            ret.append( {"sec-name": sec_name.strip(),
                        "sec-theme": sec_theme.strip(),
                        "sec-option": sec_option.strip(),
                        "sec-content": sec_content.strip()} )
            sec_name = ""
            sec_theme = ""
            sec_option = ""
            sec_content = ""
        # end for c,sec in raw_sections

        # import json
        # print(json.dumps(ret))
        return ret

    # end process_sections()

    ## Main rendering method
    def render_page(self):
        # render order:
        # opening/meta, header, sections, footer, closing
        final_out = ["", ""]  # page content + url
        opening_txt = '''
<!doctype html>
<html>
<head>
    <title> ''' + self.title + ''' </title>
    <meta charset="UTF-8">
    <meta name="author" content="''' + self.author + ''''">
    <!-- TODO: Add keywords + description meta -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<html>
'''
        closing_txt = '''
<!-- Page created by ssebsMS - https://github.com/ssebs/ssebsms -->    
</html>
'''
        final_out[0] = opening_txt
        final_out[0] += "   <!-- start header -->\n"
        final_out[0] += markdown(self.header_txt)
        final_out[0] += "\n   <!-- end header -->\n"

        for sec in self.sections:
            final_out[0] += "   <!-- start section: " + sec['sec-name'] + "-->\n"

            final_out[0] += "\n   <!-- end section: " + sec['sec-name'] + "-->\n"

        final_out[0] += "   <!-- start footer -->\n"
        final_out[0] += markdown(self.footer_txt)
        final_out[0] += "\n   <!-- end footer -->\n"

        final_out[0] += closing_txt
        return final_out   # page content + url

    # end render_page
# end class Page