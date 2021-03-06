from flask import Flask, request
from app_service import AppService
import json
import subprocess
import os

app = Flask(__name__)
appService = AppService();

# Тестовый ендпоинт для проверки состояния приложения.
@app.route('/')
def home():
    app.logger.info("App Works!!!")
    return "App Works!!!"

# Ендпоинт для подписи файлов.
@app.route(r'/api/signFiles', methods=['POST'])
def sign_file():
    input_data = request.get_json()
    output_data = []
    path = '/app/signFiles/'
        
    # Для каждого файла.
    for row in input_data:
        # Переменные.
        file_name = row['FileName']
        sign_file_name = row['FileName'] + '.sgn'
        
        # Сохранение для подписания.
        appService.save_file(app, path, file_name, row['FileBody'])
        
        # Подписание файла.
        command = 'cp /app/signFiles/' + file_name + ' /app/signFiles/' + sign_file_name
        subprocess.run(command, shell=True)

        # Формируем возвращаемые данные.
        sign_file_bytes = appService.read_file_to_bytes(app, path, sign_file_name)
        output_data.append({ "FileName": file_name, "SignFileName": sign_file_name, "FileBody": str(sign_file_bytes) })
        
        # Подчищаем за собой папку.
        os.remove(path + file_name)
        os.remove(path + sign_file_name)
    
    return json.dumps(output_data);
    
# Ендпоинт для шифрования файлов.
@app.route(r'/api/encryptFiles', methods=['POST'])
def encrypt_file():
    input_data = request.get_json()
    output_data = []
    path = '/app/encryptFiles/'
        
    # Для каждого файла.
    for row in input_data:
        # Переменные.
        file_name = row['FileName']
        encrypt_file_name = row['FileName'] + '.enc'
        
        # Сохранение для шифрования.
        appService.save_file(app, path, file_name, row['FileBody'])
        
        # Шифрование файла.
        command = 'cp /app/encryptFiles/' + file_name + ' /app/encryptFiles/' + encrypt_file_name
        subprocess.run(command, shell=True)

        # Формируем возвращаемые данные.
        encrypt_file_bytes = appService.read_file_to_bytes(app, path, encrypt_file_name)
        output_data.append({ "FileName": file_name, "EncryptFileName": encrypt_file_name, "FileBody": str(encrypt_file_bytes) })
        
        # Подчищаем за собой папку.
        os.remove(path + file_name)
        os.remove(path + encrypt_file_name)
    
    return json.dumps(output_data);

# Запуск flask.    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

