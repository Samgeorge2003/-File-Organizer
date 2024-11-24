import os
import shutil

def organize_files(directory):
    # Define file type categories and their extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"],
        "Others": []
    }

    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Organize files
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Determine the file type
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_extension in extensions:
                folder_path = os.path.join(directory, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        # Move files with unknown extensions to "Others"
        if not moved:
            others_path = os.path.join(directory, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, os.path.join(others_path, file))

    print("Files organized successfully!")

# Example usage
if __name__ == "__main__":
    target_directory = input("Enter the path to the directory you want to organize: ")
    organize_files(target_directory)
