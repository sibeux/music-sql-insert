import os
import json
import mutagen
import glob

def get_audio_metadata(filepath):
    try:
        f = mutagen.File(filepath, easy=True)
        if f:
            title = f.get('title', [None])[0]
            artist = f.get('artist', [None])[0]
            album = f.get('album', [None])[0]
            albumartist = f.get('albumartist', [None])[0]
            return {'title': title, 'artist': artist, 'album': album, 'albumartist': albumartist}
    except Exception as e:
        pass
    
    # Try non-easy if easy fails
    try:
        f = mutagen.File(filepath)
        if f:
            # this is very format-dependent, just try some common keys
            title = f.get('TIT2', f.get('\xa9nam', [None]))
            if title and hasattr(title, 'text'): title = title.text[0]
            artist = f.get('TPE1', f.get('\xa9ART', [None]))
            if artist and hasattr(artist, 'text'): artist = artist.text[0]
            return {'title': title, 'artist': artist}
    except:
        pass
    return {}

def main():
    folders = [
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\chainsaw-man-the-movie-reze-arc-original-soundtrack-summers-end-special-edition-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\choucho-defy-the-silence-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\illit-i-got-your-back-2026-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\little-glee-monster-jupiter-from-the-first-take-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\machico-fantastic-dreamer-10th-anniversary-arrange-ver-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\summitpunpeevavaomsb-oddtaxi-original-soundtrack-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\tada-utsukushii-noroi-nakamura-hak-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\yoko-takahashi-nyankoku-na-nyanko-no-thesis-single-20260802-204817",
        r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\yoko-takahashi-the-cruel-angels-thesis-20260802-204817"
    ]
    
    result = {}
    for folder in folders:
        if not os.path.exists(folder):
            continue
            
        folder_info = {
            'txt_files': {},
            'discs': {}
        }
        
        # Read txt files in root
        for txt_file in glob.glob(os.path.join(folder, '*.txt')):
            if not txt_file.endswith('.here.txt'):
                with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
                    folder_info['txt_files'][os.path.basename(txt_file)] = f.read().strip()
                    
        # Check subfolders for audio files
        for sub in os.listdir(folder):
            sub_path = os.path.join(folder, sub)
            if os.path.isdir(sub_path):
                # if 'flac', '1', '2' etc
                if sub == 'flac' or sub.isdigit():
                    disc_key = "1" if sub == 'flac' else sub
                    folder_info['discs'][disc_key] = []
                    
                    audio_files = []
                    for ext in ('*.flac', '*.opus', '*.mp3', '*.m4a', '*.wav'):
                        audio_files.extend(glob.glob(os.path.join(sub_path, ext)))
                        
                    for af in sorted(audio_files):
                        meta = get_audio_metadata(af)
                        folder_info['discs'][disc_key].append({
                            'filename': os.path.basename(af),
                            'metadata': meta
                        })
        result[os.path.basename(folder)] = folder_info
        
    with open(r'c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\generator\extracted_data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
