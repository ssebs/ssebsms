###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
##

# imports
import os,shutil

# test definition for import testing
def init_test(my_arg):
    print("I'm in the _init.py file! Even " + str(my_arg) + " is here!")


# check if public/ dir is created, if not, create it.
def check_output_folder(site_name):
    folders = ["public", site_name]

    for fn in folders:
        if fn in os.listdir("../"):
            print("Don't need to initialize, clean first if you want to restart.")
        else:
            os.mkdir("../" + fn + "/", mode=0o644)
            print("Created " + fn + "/ directory for generated files.")

# end check_output_folder()

#
def copy_skel(site_name):
    site_name = "mysite"
    shutil.copytree("../skel/", "../" + site_name + "/")
    print("Copied contents of skel/ to " + site_name + "/")
    print("\nModify the contents of " + site_name + "/" + " and run 'python ssebsMS.py build' to build the generated HTML.")
# end copy_skel()

# entry of init module
def entry():
    site_name = "mysite"
    check_output_folder(site_name)
    copy_skel(site_name)
# end entry()

## Code entry for testing ##
entry()