import os
import zipfile
import shutil

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

        # Open the zip file
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            # Loop through each file in the zip file
            for file in zip_ref.namelist():
                # Construct the path where the file would be if it was in the Daz library
                daz_filepath = os.path.join(daz_library_path, file)

                # Check if the file already exists in the Daz library
                if os.path.exists(daz_filepath):
                    print(f"The file {file} already exists in the Daz library.")
                else:
                    print(f"The file {file} does not exist in the Daz library. Do you want to install it? (yes/no)")
                    answer = input()

                    # If the user wants to install the file, extract it to the Daz library
                    if answer.lower() == "yes":
                        zip_ref.extract(file, daz_library_path)
                        print(f"The file {file} has been installed to the Daz library.")

        # After installing the content of the zip file, move the zip file to the specified folder
        shutil.move(filepath, os.path.join(zip_files_folder_path, filename))
        print(f"The zip file {filename} has been moved to {zip_files_folder_path}.")
