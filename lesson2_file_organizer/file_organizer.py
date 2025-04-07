import os
import shutil


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".js", ".html", ".css"]
}

TARGET_FOLDER = "test_folder"


# FUNCTION FOR ORGANIZING 
def organize_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    destination = os.path.join(folder, folder_name)

                    if not os.path.exists(destination):
                        os.makedirs(destination)

                    shutil.move(file_path, os.path.join(destination, filename))
                    print(f"Moved {filename} -> {folder_name}")
                    break

if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)



