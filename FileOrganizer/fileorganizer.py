import os

# Folders and their respective file extensions
ORGANIZATION = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mkv", ".flv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"]
}

def organize_files(directory):
    for folder, extensions in ORGANIZATION.items():
        folder_path = os.path.join(directory, folder)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Loop through files and move them to respective directories
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            # Check if it's a file (and not a directory/folder)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1]
                
                # If the file extension matches, move it to the respective folder
                if file_extension in extensions:
                    target_path = os.path.join(folder_path, filename)
                    os.rename(file_path, target_path)
                    print(f"Moved {filename} to {folder}/")

if __name__ == "__main__":
    # Organize files in the current directory
    current_directory = os.getcwd()
    organize_files(current_directory)
