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


# check if dir is created, if not, create it.
def check_output_folder(site_name):
    if site_name in os.listdir("./"):
        print("Don't need to initialize, clean first if you want to restart.")
        return 1
    else:
        return 0
# end check_output_folder()

# set the ENV file if exists
def set_ENV(site_name, env_filename):
    if env_filename in os.listdir("./"):
        # set site-name line with the new site-name
        beginning = '''## ssebsMS-ENV - environment vars for ssebsMS
# Sample below.
# site-name = my_site    
'''
        with open(env_filename, "w") as f:
            f.write(beginning)
            f.write("site-name = " + site_name + "\n")
        print("Setting " + env_filename + " site-name = " + site_name)
# end set_ENV()

#
def copy_skel(site_name):
    #print("cp ./skel/", "./" + site_name + "/")
    shutil.copytree("./skel/", "./" + site_name + "/")
    print("Copied contents of skel/ to " + site_name + "/")
    print("\nModify the contents of " + site_name + "/" + " and run 'python ssebsMS.py build " + site_name + "' to build the generated HTML.")
# end copy_skel()

# entry of init module
def init_entry(site_name, env_filename):
    if not check_output_folder(site_name):
        copy_skel(site_name)
        set_ENV(site_name, env_filename)
    else:
        return 1
# end entry()
