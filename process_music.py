import os
import re
import json
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

# Install mutagen if not available
try:
    import mutagen
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mutagen"])
    import mutagen

def contains_japanese(text):
    if not text: return False
    return any('\u4e00' <= char <= '\u9fff' or '\u3040' <= char <= '\u309f' or '\u30a0' <= char <= '\u30ff' for char in text)

def get_metadata(filepath):
    try:
        f = mutagen.File(filepath, easy=True)
        if f:
            artist = f.get('artist', [None])[0]
            title = f.get('title', [None])[0]
            return artist, title
    except Exception as e:
        pass
    return None, None

def parse_txt_for_album_info(txt_file):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f if l.strip()]
    except UnicodeDecodeError:
        try:
            with open(txt_file, 'r', encoding='shift-jis') as f:
                lines = [l.strip() for l in f if l.strip()]
        except Exception:
            with open(txt_file, 'r', encoding='latin1') as f:
                lines = [l.strip() for l in f if l.strip()]
                
    if not lines:
        return "Unknown Album", "Unknown Artist"
        
    line1 = lines[0]
    
    if " / " in line1:
        parts = line1.split(" / ", 1)
        return parts[0].strip(), parts[1].strip()
        
    if len(lines) == 1 or (len(lines) > 1 and lines[1].lower().startswith("disc ")):
        if " - " in line1:
            parts = line1.split(" - ", 1)
            return parts[1].strip(), parts[0].strip()
            
    if len(lines) > 1 and not lines[1].lower().startswith("disc "):
        return line1, lines[1]
        
    return line1, "Unknown Artist"

def process_folder(base_dir):
    print(f"\nProcessing folder: {base_dir}")
    if not os.path.isdir(base_dir):
        print("  [!] Directory not found.")
        return

    # Find the descriptive txt file
    txt_file = None
    for f in os.listdir(base_dir):
        if f.lower().endswith('.txt') and not f.lower().startswith('example') and f.lower() != '.here.txt':
            txt_file = os.path.join(base_dir, f)
            break
            
    if txt_file:
        album_title, album_artist = parse_txt_for_album_info(txt_file)
    else:
        album_title, album_artist = "Unknown Album", "Unknown Artist"
        
    print(f"  Album Title: {album_title}")
    print(f"  Album Artist: {album_artist}")

    # Determine discs
    disc_folders = []
    if os.path.isdir(os.path.join(base_dir, "flac")):
        disc_folders.append(("0", os.path.join(base_dir, "flac")))
    else:
        # Check for 1, 2, etc.
        for item in os.listdir(base_dir):
            if item.isdigit() and os.path.isdir(os.path.join(base_dir, item)):
                disc_folders.append((item, os.path.join(base_dir, item)))
    
    disc_folders.sort(key=lambda x: int(x[0]))
    
    # Initialize .here.txt dictionary
    max_disc = "0"
    if disc_folders and disc_folders[-1][0] != "0":
        max_disc = disc_folders[-1][0]
        
    here_dict = {
        "category": "2",
        "title": album_title,
        "author": album_artist,
        "disc": max_disc,
        "music_name_index": {},
        "id_category_list": {
            "1": "IndoPride",
            "2": "日本の歌",
            "3": "Jowo Mletre",
            "4": "Worldwide",
            "5": "Instrumental"
        },
        "source": "discord"
    }
    
    total_tracks = 0
    
    for disc_str, disc_path in disc_folders:
        key_str = "1" if disc_str == "0" else disc_str
        here_dict[key_str] = []
        here_dict["music_name_index"][key_str] = []
        
        audio_files = []
        for f in os.listdir(disc_path):
            if os.path.isfile(os.path.join(disc_path, f)) and f.lower().endswith(('.flac', '.mp3', '.m4a', '.wav', '.opus', '.ogg')):
                audio_files.append(f)
                
        def get_prefix(filename):
            match = re.match(r'^(?:\d+\.)?(\d+)', filename)
            return int(match.group(1)) if match else 999
        audio_files.sort(key=get_prefix)
        
        for filename in audio_files:
            total_tracks += 1
            filepath = os.path.join(disc_path, filename)
            
            meta_artist, meta_title = get_metadata(filepath)
            
            artist_from_meta = meta_artist if meta_artist and not contains_japanese(meta_artist) else None
            title_from_meta = meta_title if meta_title and not contains_japanese(meta_title) else None
            
            # Parse filename
            match = re.match(r'^(?:\d+\.)?(\d+)[.\s]+(.+?)\.([a-zA-Z0-9]+)$', filename)
            if match:
                index_str, rest, ext = match.groups()
                index_str = str(int(index_str)).zfill(2)
                
                file_artist = album_artist
                file_title = rest
                if " - " in rest:
                    parts = rest.split(" - ", 1)
                    if parts[0].strip().lower() == album_artist.lower():
                        file_artist = parts[0].strip()
                        file_title = parts[1].strip()
            else:
                index_str = str(total_tracks).zfill(2)
                file_artist = album_artist
                file_title = filename
                ext = filename.rsplit('.', 1)[-1] if '.' in filename else "opus"
                
            final_artist = artist_from_meta if artist_from_meta else file_artist
            final_title = title_from_meta if title_from_meta else file_title
            
            here_dict[key_str].append(f"{index_str} --- {final_artist}")
            here_dict["music_name_index"][key_str].append(f"{index_str} --- {final_title}")
            
            # Rename file
            new_filename = f"{index_str}.{ext}"
            new_filepath = os.path.join(disc_path, new_filename)
            
            if filepath != new_filepath:
                os.rename(filepath, new_filepath)
                print(f"  Renamed: {filename} -> {new_filename}")

    # Write .here.txt
    here_txt_path = os.path.join(base_dir, ".here.txt")
    with open(here_txt_path, 'w', encoding='utf-8') as f:
        json.dump(here_dict, f, ensure_ascii=False, indent=2)
    print(f"  Generated .here.txt")
    
    # Rename base directory to prepend track count
    if total_tracks > 0:
        parent_dir = os.path.dirname(base_dir)
        old_basename = os.path.basename(base_dir)
        new_basename = f"{total_tracks}-{old_basename}"
        new_base_path = os.path.join(parent_dir, new_basename)
        
        if not os.path.exists(new_base_path) and old_basename != new_basename:
            os.rename(base_dir, new_base_path)
            print(f"  Renamed folder: {old_basename} -> {new_basename}")
            
if __name__ == "__main__":
    target_folders = [
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\witch-hat-atelier-original-soundtrack-20260712-004325"
    ]
    
    for folder in target_folders:
        process_folder(folder)
