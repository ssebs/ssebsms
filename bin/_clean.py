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
    print("I'm in the _init.py file! Even " + str(my_arg) + " is here!")

# check if dir exists, if so, delete it
def delete_folder_if_exist(site_name):
    if site_name in os.listdir("../"):
        ans = input("Are you sure you want to delete " + site_name + "? ")
        if "y" in ans.lower():
            shutil.rmtree("../" + site_name)
            print(site_name + " has been deleted.")
        else:
            print(site_name + " not deleted.")
        return 0
    else:
        print(site_name + " not found or deleted.")
        return 1
# end check_output_folder()

# entry of init module
def clean_entry(site_name):
    return delete_folder_if_exist(site_name)
# end entry()
