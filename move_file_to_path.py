import os
import shutil

def move_txt_files(source_folder, destination_folder):

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


    files = [f for f in os.listdir(source_folder) if f.endswith(".txt")]


    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"File '{file}' moved to '{destination_folder}'")

if __name__ == "__main__":

    source_folder = "data_for_learn/train/images"
    destination_folder = "data_for_learn/valid/labels"


    move_txt_files(source_folder, destination_folder)

    print("Процесс завершен.")
