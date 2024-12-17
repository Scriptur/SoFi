import os
import time
from datetime import datetime
from pathlib import Path
import shutil

# Питання чи потрібно виводити інформацію
user_answer = input("Виводити технічну інформацію (n) ? (y/n) ").lower()
print("")

# Поточний робочий каталог
current_directory = os.getcwd()
if user_answer == "y":
    print("Поточний робочий каталог:", current_directory)
    print("")
# Отримуємо список файлів, виключаючи файл скрипта (SoFi.py) та виконуючий файл (SoFi.exe)
files = [f for f in os.listdir(current_directory)
        if os.path.isfile(os.path.join(current_directory, f)) and f !='SoFi.py' and f !='SoFi.exe']

# Виводимо список файлів
for file in files:
    if user_answer == "y":
        print("Файли в теці:")
        print(f"    Назва файла: {file}")
    # Отримуємо інформацію про файл
    file_stats = os.stat(file)
    if user_answer == "y":
        # Виводимо отриману інформацію
        print(f"Отримана інформація:")
        print(f"    {file_stats}")

    # Дата створення
    creation_time = file_stats.st_ctime
    date_create = datetime.fromtimestamp(creation_time)
    creation_time_local = time.localtime(creation_time)
    format_creation_time = time.strftime('%Y-%m-%d', creation_time_local)
    
    # Дата змін
    time_change = file_stats.st_mtime
    date_change = datetime.fromtimestamp(time_change)
    time_change_local = time.localtime(time_change)
    format_time_change = time.strftime('%Y-%m-%d', time_change_local)

    if date_create < date_change:
        folder_name = format_creation_time
        if user_answer == "y":
            print(f"Дата створення: {folder_name}")
    else:
        folder_name = format_time_change
        if user_answer == "y":
            print(f"Дата зміни: {folder_name}")
    
    folder_path = Path(folder_name)
    if not folder_path.exists():
        folder_path.mkdir()
        if user_answer == "y":
            print(f"Теку {folder_name} створено")
    else:
        if user_answer == "y":
            print(f"Тека {folder_name} вже існує")

    destination_path = os.path.join(folder_path, file)

    if os.path.exists(destination_path):
        print(f"Файл '{file}' вже існує в теці {folder_path} ")
    else:
        shutil.move(file, destination_path)
        print(f"Файл '{file}' переміщено в теку {folder_path} ")
    
    if user_answer == "y":
        print("")
    
print("Програма завершена.")
input("Натисніть Enter, щоб закрити...")