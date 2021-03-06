import json

class AppService:

    # Сохранение файла в директорию.
    def save_file(self, app, path, file_name, file_body):
        with open(path + file_name,  mode='wb') as file:
            file.write(bytes(bytearray(file_body)))

    # Чтение файла из директории.
    def read_file_to_bytes(self, app, path, file_name):
        with open(path + file_name,  mode='rb') as file:
            data = file.read()
            return [d for d in data]
                    