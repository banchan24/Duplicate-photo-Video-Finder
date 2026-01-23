import os

#Ask user where to look
folder = input("Enter a folder path: ")

#File Types
media_extensions = [ ".jpg", ".jpeg", ".png", ".webp", ".gif", ".mp4", ".mov", ".mkv", ".avi"]

print ("\nMedia files found: \n")

#Looping through each item in the folder
for current_folder, subfolders, filenames in os.walk(folder):
    for name in filenames:
        lower_name = name.lower()

        #Check file extension
        for ext in media_extensions:
            if lower_name.endswith(ext):
                full_path = os.path.join(current_folder, name)
                
                #Get file size in bytes
                try:
                    size = os.path.getsize(full_path)
                except OSError:
                    #Skip files if can't access
                    continue

                print (f"{full_path} | {size} bytes")
                break

