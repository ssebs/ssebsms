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
def clean_test(my_arg):
    print("I'm in the _clean.py file! Even " + str(my_arg) + " is here!")

# check if dir exists, if so, delete it
def delete_folder_if_exist(site_name, env_filename):
    if site_name in os.listdir("./"):
        if site_name == "skel":
            print("Do not delete/clean the skel/ directory!")
            return 1
        ans = input("Are you sure you want to delete " + str(site_name) + "? ")
        if "y" in ans.lower():
            # clear site_name/ dir
            shutil.rmtree("./" + site_name)

            # reset env
            os.remove("./" + env_filename)
            with open(env_filename,"w") as f:
                beginning = '''## ssebsMS-ENV - environment vars for ssebsMS
# Sample below.
# site-name = my_site    
'''
                f.write(beginning)
            print(site_name + " has been deleted.")
        else:
            print(site_name + " not deleted.")
        return 0
    else:
        print(site_name + " not found or deleted.")
        return 1
# end check_output_folder()

# entry of clean module
def clean_entry(site_name, env_filename):
    return delete_folder_if_exist(site_name, env_filename)
# end entry()
