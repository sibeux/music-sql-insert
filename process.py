import os
import re
import json
import mutagen

def get_audio_metadata(file_path):
    try:
        audio = mutagen.File(file_path, easy=True)
        if audio is None:
            audio = mutagen.File(file_path)
            
        artist = None
        if audio:
            if 'artist' in audio:
                artist = audio['artist'][0]
            elif 'TPE1' in audio:
                artist = audio['TPE1'].text[0]
            elif '©ART' in audio:
                artist = audio['©ART'][0]
                
        return artist
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def has_japanese(text):
    if not text:
        return False
    return bool(re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', text))

def parse_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.read().splitlines()]
    
    album_title = lines[0] if len(lines) > 0 else "Unknown Album"
    album_author = lines[1] if len(lines) > 1 else "Unknown Author"
    
    tracks = {}
    current_track = 1
    for i in range(2, len(lines)):
        if lines[i] == str(current_track):
            if i + 1 < len(lines):
                tracks[current_track] = lines[i+1]
                current_track += 1
                
    return album_title, album_author, tracks

def process_album(album_dir):
    print(f"Processing album: {album_dir}")
    txt_files = [f for f in os.listdir(album_dir) if f.endswith('.txt') and f.lower() not in ['.here.txt', 'discord.txt', 'example.txt']]
    
    album_title = "Unknown Album"
    album_author = "Unknown Author"
    romanized_tracks = {}
    
    if txt_files:
        txt_path = os.path.join(album_dir, txt_files[0])
        album_title, album_author, romanized_tracks = parse_txt(txt_path)
        
    disc_folders = []
    if os.path.exists(os.path.join(album_dir, 'flac')):
        disc_folders.append(('1', os.path.join(album_dir, 'flac')))
    else:
        for i in range(1, 10):
            df = os.path.join(album_dir, str(i))
            if os.path.exists(df):
                disc_folders.append((str(i), df))
                
    if not disc_folders:
        print(f"No audio folders (flac or 1,2,..) found in {album_dir}")
        return
        
    is_multi_disc = len(disc_folders) > 1 or (len(disc_folders) == 1 and disc_folders[0][0] != '1' and not os.path.exists(os.path.join(album_dir, 'flac')))
    if os.path.exists(os.path.join(album_dir, '1')) or os.path.exists(os.path.join(album_dir, '2')):
        is_multi_disc = True
        
    disc_val = "1" if is_multi_disc else "0"
    
    out_authors = {"1": [], "2": [], "3": [], "4": []}
    out_titles = {"1": [], "2": [], "3": [], "4": []}
    
    track_global_idx = 1
    total_tracks = 0
    
    for disc_num, disc_path in disc_folders:
        audio_files = []
        for f in os.listdir(disc_path):
            if f.lower().endswith(('.flac', '.mp3', '.m4a', '.wav', '.opus', '.ogg', '.aac')):
                audio_files.append(f)
                
        # Sort files to process them in order
        audio_files.sort()
        
        for idx, af in enumerate(audio_files):
            total_tracks += 1
            idx_str = f"{idx+1:02d}"
            af_path = os.path.join(disc_path, af)
            
            # Get title
            title = romanized_tracks.get(track_global_idx)
            if not title:
                # remove extension and numbers
                name_no_ext = os.path.splitext(af)[0]
                name_clean = re.sub(r'^\d+[\s\.\-]*', '', name_no_ext)
                title = name_clean
                
            # Get author
            meta_artist = get_audio_metadata(af_path)
            if not meta_artist or has_japanese(meta_artist):
                track_author = album_author
            else:
                track_author = meta_artist
                
            out_titles[disc_num].append(f"{idx_str} --- {title}")
            out_authors[disc_num].append(f"{idx_str} --- {track_author}")
            
            track_global_idx += 1
            
            # Rename file
            ext = os.path.splitext(af)[1]
            new_af = f"{idx_str}{ext}"
            new_af_path = os.path.join(disc_path, new_af)
            if af_path != new_af_path:
                os.rename(af_path, new_af_path)
                
    # write .here.txt
    here_data = {
        "1": out_authors["1"],
        "2": out_authors["2"],
        "3": out_authors["3"],
        "4": out_authors["4"],
        "category": "2",
        "title": album_title,
        "author": album_author,
        "disc": disc_val,
        "music_name_index": {
            "1": out_titles["1"],
            "2": out_titles["2"],
            "3": out_titles["3"],
            "4": out_titles["4"]
        },
        "id_category_list": {
            "1": "IndoPride",
            "2": "日本の歌",
            "3": "Jowo Mletre",
            "4": "Worldwide",
            "5": "Instrumental"
        },
        "source": "discord"
    }
    
    here_path = os.path.join(album_dir, '.here.txt')
    with open(here_path, 'w', encoding='utf-8') as f:
        # Do custom writing to exactly match standard JSON but we can just use json.dump
        json.dump(here_data, f, indent=2, ensure_ascii=False)
        
    # rename album folder
    parent_dir = os.path.dirname(album_dir)
    old_folder_name = os.path.basename(album_dir)
    
    # check if already has number prefix
    if re.match(r'^\d+-', old_folder_name):
        return
        
    new_folder_name = f"{total_tracks}-{old_folder_name}"
    new_album_dir = os.path.join(parent_dir, new_folder_name)
    os.rename(album_dir, new_album_dir)
    print(f"Renamed album folder: {old_folder_name} -> {new_folder_name}")

if __name__ == '__main__':
    base_dir = r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong"
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            process_album(item_path)
