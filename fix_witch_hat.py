import json
import os
import re

base_dir = r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong\46-witch-hat-atelier-original-soundtrack-20260712-004325"
txt_path = os.path.join(base_dir, "New Text Document.txt")
json_path = os.path.join(base_dir, ".here.txt")

with open(txt_path, 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]

tracks_disc1 = []
tracks_disc2 = []

current_disc = 0
for line in lines:
    if "Disc 1" in line:
        current_disc = 1
    elif "Disc 2" in line:
        current_disc = 2
    elif current_disc > 0:
        # Match '01 \tVoice of Magic \t6:14' or '01 Voice of Magic 6:14'
        # The line might not have a time if it's the last track (like track 24 in disc 1 doesn't have a time in the preview)
        # Ah wait, let's just split by tab or first space
        m = re.match(r'^(\d+)\s+(.+)$', line)
        if m:
            index = str(int(m.group(1))).zfill(2)
            title = m.group(2).strip()
            # remove trailing time if exists
            title = re.sub(r'\s+\d+:\d+$', '', title).strip()
            entry = f"{index} --- {title}"
            if current_disc == 1:
                tracks_disc1.append(entry)
            elif current_disc == 2:
                tracks_disc2.append(entry)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# The parsing might miss tracks if regex is wrong, so ensure length
if len(tracks_disc1) > 0 and len(tracks_disc2) > 0:
    data["music_name_index"]["1"] = tracks_disc1
    data["music_name_index"]["2"] = tracks_disc2
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Fixed witch-hat-atelier .here.txt with Romanized names!")
else:
    print("Error parsing text file")
