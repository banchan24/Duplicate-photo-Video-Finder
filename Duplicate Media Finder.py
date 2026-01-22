import os

#Ask user where to look
folder = input("Enter a folder path: ")

#File Types
media_extensions = [ ".jpg", ".jpeg", ".png", ".webp", ".gif", ".mp4", ".mov", ".mkv", ".avi"]

print ("\nMedia files found: \n")

#Looping through each item in the folder
for name in os.walk(folder):
    #Making the name lowercase so both JPG and jpg both work
    lower_name = name.lower()
    #Checking if the filename ends with any extension in the list
    for ext in media_extensions:
        if lower_name.endswith(ext):
            print(name)
            break #Stop checking other extensions for this file 
# os.walk goes through all folders and subfolders
for current_folder, subfolders, filenames in os.walk(folder):
    for name in filenames:
        lower_name = name.lower()

        #Check file extension
        for ext in media_extensions:
            if lower_name.endswith(ext):
                full_path = os.path.join(current_folder, name)
                print(full_path)
                break
