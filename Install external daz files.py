import os
import zipfile
import shutil
import time  # import the time module

# Define the path to your Daz library and the new folder
daz_library_path = "D:/Daz Data/My Library"
new_folder_path = os.path.expandvars("%userprofile%/downloads")
zip_files_folder_path = "D:/Daz zip Files"

# Loop through each file in the new folder
for filename in os.listdir(new_folder_path):
    # Check if the file is a zip file
    if filename.endswith(".zip"):
        # Construct the full file path
        filepath = os.path.join(new_folder_path, filename)

        try:
            # Open the zip file
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                # Check if any file in the zip file does not exist in the Daz library
                if not all(os.path.exists(os.path.join(daz_library_path, file)) for file in zip_ref.namelist()):
                    print(f"The files in this zip folder {filename} do not exist in the Daz library. Do you want to copy them? (yes/no)")
                    answer = input().lower()

                    # If the user wants to install the files, extract them to the Daz library
                    if answer.lower() in ["yes", "y"]:
                        zip_ref.extractall(daz_library_path)
                        print(f"The files from {filename} have been installed to the Daz library.")

                        # After installing the content of the zip file, copy the zip file to the specified folder
                        shutil.copy(filepath, os.path.join(zip_files_folder_path, filename))
                        print(f"The zip file {filename} has been copied to {zip_files_folder_path}.")

                        # Add a delay before removing the file
                        time.sleep(1)  # wait for 1 second

                        # Remove the original zip file
                        os.remove(filepath)
                        print(f"The original zip file {filename} has been removed from {new_folder_path}.")
        except zipfile.BadZipFile:
            print(f"The zip file {filename} is corrupted or invalid. Skipping this file.")
        except PermissionError:
            print(f"The file {filename} is currently in use by another process. Would you like to wait and retry? (yes/no)")
            answer = input().lower()
            if answer.lower() in ["yes", "y"]:
                print("Waiting for 5 seconds before retrying...")
                time.sleep(5)  # wait for 5 seconds
                continue  # retry the current iteration of the loop
            else:
                print(f"Skipping the file {filename}.")
