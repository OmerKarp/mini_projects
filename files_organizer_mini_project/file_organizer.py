import os
import shutil

# Set the directory to organize (put everything you wanna organize there!!!)
directory = os.getcwd() + '\\file_organizer_folder'

# Define file extensions and their corresponding folders
file_extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css', '.sh', '.bat'],
    'Executables': ['.exe', '.msi']
}

def organize_files():
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            
            for folder, extensions in file_extensions.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    moved = True
                    break
            
            if not moved:
                other_folder = os.path.join(directory, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))
                
    print("Files have been organized successfully.")

if __name__ == "__main__":
    organize_files()
