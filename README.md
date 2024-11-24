# File-Organizer
A file organizer script helps manage files in a directory by sorting them into subfolders based on file type.
# How it Works:
* Categories: The script uses predefined categories (file_types) with associated file extensions.
* Folders: For each file in the target directory, the script:
          * Checks its extension.
          * Moves it to the appropriate folder (e.g., "Images," "Documents").
* Unknown Types: Files with unrecognized extensions are moved to an "Others" folder.
* Directories: Existing subdirectories are ignored.
# Usage:
* Save this script as file_organizer.py.
* Run it in the terminal or Python IDE
* Enter the path of the directory want to organize.
* The script will sort files into subfolders within the same directory.
