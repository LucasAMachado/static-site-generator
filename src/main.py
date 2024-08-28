
import os
import shutil


def main():
   source_to_destination()


def source_to_destination():
    directory_file_path = "./public"
    source_file = "./static"

    delete_files_in_directory(directory_file_path)
    copy_files_from_one_directory_to_another(source_file, directory_file_path)


def delete_files_in_directory(directory_file_path) -> None:
    try:
        files = os.listdir(directory_file_path)
        for file in files:
            file_path = os.path.join(directory_file_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        print("All of the files have been deleted")
    except OSError:
        print("Error occurred while deleting the files in,", directory_file_path)


def copy_files_from_one_directory_to_another(source_file, destination_file) -> None:

    image_dir = os.path.join(destination_file, "images")
    os.makedirs(image_dir, exist_ok=True)

    # Copy all files and directories from source to destination
    for item in os.listdir(source_file):
        source_item = os.path.join(source_file, item)
        destination_item = os.path.join(destination_file, item)

        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, destination_item)

    print(f"The files have been copied over from {source_file} to {destination_file}")            


    
if __name__ == "__main__":
    main()
