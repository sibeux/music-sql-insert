from pathlib import Path

# Base directory (current script directory or custom path)
BASE_DIR = Path(r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD")
# If running directly inside the target directory, you can also use:
# BASE_DIR = Path(__file__).resolve().parent

folder_names = [
    "1-indopride",
    "2-Anisong",
    "3-jowomletre",
    "4-worldwide",
    "5-instrumental",
]

for name in folder_names:
    folder_path = BASE_DIR / name
    if folder_path.exists():
        print(f"Skipped (already exists): {folder_path.name}")
    else:
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created: {folder_path.name}")
