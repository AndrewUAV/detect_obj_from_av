import os

def delete_every_third_photo(folder_path):
    try:
        # Получаем список файлов в указанной директории
        files = os.listdir(folder_path)

        # Определяем, какие файлы являются изображениями
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        # Удаляем каждую третью фотографию
        for i in range(2, len(image_files), 3):
            file_to_delete = os.path.join(folder_path, image_files[i])
            os.remove(file_to_delete)
            print(f'Удалена фотография: {image_files[i]}')

        print('Удаление завершено.')

    except Exception as e:
        print(f'Произошла ошибка: {e}')

# Укажите путь к вашей папке с фотографиями
folder_path = 'data_for_learn/photo_from_video'
delete_every_third_photo(folder_path)
