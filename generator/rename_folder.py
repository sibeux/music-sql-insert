import os
import re
from datetime import datetime

def slugify(text):
    # lowercase
    text = text.lower()
    # hapus karakter selain huruf, angka, dan spasi
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    # ganti spasi dan dash berlebih jadi satu dash
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def rename_folders(base_path):
    if not os.path.exists(base_path):
        print("Path tidak ditemukan")
        return

    for folder_name in os.listdir(base_path):
        old_path = os.path.join(base_path, folder_name)

        if os.path.isdir(old_path):
            clean_name = slugify(folder_name)

            # timestamp unik
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

            new_name = f"{clean_name}-{timestamp}"
            new_path = os.path.join(base_path, new_name)

            # hindari konflik nama
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{clean_name}-{timestamp}-{counter}"
                new_path = os.path.join(base_path, new_name)
                counter += 1

            os.rename(old_path, new_path)
            print(f"Renamed: {folder_name} -> {new_name}")

if __name__ == "__main__":
    # base_path = input("Masukkan path folder: ").strip()
    list_base_path = [
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\1-indopride",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong",
        r"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\4-worldwide",
        r"C:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\5-instrumental"
    ]
    for base_path in list_base_path:
        rename_folders(base_path)