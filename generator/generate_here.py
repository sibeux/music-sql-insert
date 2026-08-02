import os
import json
import glob
import re

kanji_map = {
    "ジェーンは教会で眠った": "Jane wa Kyoukai de Nemutta",
    "レゼ (上田麗奈)": "Reze (Reina Ueda)",
    "ただ美しい呪い": "Tada Utsukushii Noroi",
    "夜に浮かぶ": "Yoru ni Ukabu",
    "光り": "Hikari",
    "ただ美しい呪い (Anime ver.)": "Tada Utsukushii Noroi (Anime ver.)",
    "夜に浮かぶ (Anime ver.)": "Yoru ni Ukabu (Anime ver.)",
    "光り (Anime ver.)": "Hikari (Anime ver.)",
    "スカートとPUNPEE": "Skirt to PUNPEE",
    "三森すずこ": "Suzuko Mimori"
}

def clean_kanji(text):
    if not text:
        return ""
    for k, v in kanji_map.items():
        text = text.replace(k, v)
    return text

def parse_txt(txt_content):
    txt_content = txt_content.replace('—', '-')
    
    if "Nakamura Hak" in txt_content:
        return {"title": "TV Anime \"Tongari Boushi no Atelier\" ED Theme \"Tada Utsukushii Noroi\"", "author": "Nakamura Hak"}
    
    if "/" in txt_content:
        parts = txt_content.split("/", 1)
        return {"title": parts[0].strip(), "author": parts[1].strip()}
    
    if "-" in txt_content:
        parts = txt_content.split("-", 1)
        return {"title": parts[1].strip(), "author": parts[0].strip()}
        
    return {"title": txt_content.strip(), "author": "Unknown"}

def process_album():
    with open('extracted_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    base_dir = r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong"
    
    for folder_name, info in data.items():
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_path):
            continue
            
        txt_files = info.get('txt_files', {})
        txt_content = ""
        for name, content in txt_files.items():
            if name != "Discord.txt" and "cue" not in name.lower() and "log" not in name.lower():
                txt_content = content
                break
                
        album_info = parse_txt(txt_content)
        
        here_data = {
            "1": [], "2": [], "3": [], "4": [],
            "category": "2",
            "title": clean_kanji(album_info["title"]),
            "author": clean_kanji(album_info["author"]),
            "disc": "0",
            "music_name_index": {
                "1": [], "2": [], "3": [], "4": []
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
        
        total_songs = 0
        discs = info.get('discs', {})
        
        if len(discs) > 1 or any(d not in ["1", "flac"] for d in discs.keys()):
            here_data["disc"] = "1"
            
        for disc_key in ["1", "2", "3", "4"]:
            if disc_key in discs:
                audio_files = discs[disc_key]
                for idx, af in enumerate(audio_files):
                    total_songs += 1
                    track_num = str(idx + 1).zfill(2)
                    
                    meta = af.get('metadata', {})
                    song_title = clean_kanji(meta.get('title', ''))
                    song_artist = clean_kanji(meta.get('artist', ''))
                    
                    if not song_title:
                        fn = af['filename']
                        fn = os.path.splitext(fn)[0]
                        fn = re.sub(r'^\d+\.\s*', '', fn)
                        song_title = clean_kanji(fn)
                        
                    if not song_artist:
                        song_artist = clean_kanji(album_info["author"])
                        
                    here_data[disc_key].append(f"{track_num} --- {song_artist}")
                    here_data["music_name_index"][disc_key].append(f"{track_num} --- {song_title}")
                    
                    subfolder = "flac" if (disc_key == "1" and os.path.exists(os.path.join(folder_path, "flac"))) else disc_key
                    old_af_path = os.path.join(folder_path, subfolder, af['filename'])
                    ext = os.path.splitext(af['filename'])[1]
                    new_af_name = f"{track_num}{ext}"
                    new_af_path = os.path.join(folder_path, subfolder, new_af_name)
                    
                    if os.path.exists(old_af_path) and old_af_path != new_af_path:
                        os.rename(old_af_path, new_af_path)
                        
        with open(os.path.join(folder_path, '.here.txt'), 'w', encoding='utf-8') as f:
            json.dump(here_data, f, indent=2, ensure_ascii=False)
            
        new_folder_name = f"{total_songs}-{folder_name}"
        new_folder_path = os.path.join(base_dir, new_folder_name)
        if folder_path != new_folder_path:
            os.rename(folder_path, new_folder_path)
            print(f"Renamed folder to {new_folder_name}")

if __name__ == '__main__':
    process_album()
