import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong"

albums_data = {
    'bow-and-arrow-20260920-140154': {
        'title': 'TV Anime "Medalist" OP Theme "BOW AND ARROW"',
        'author': 'Kenshi Yonezu',
        'disc': '0',
        'tracks': [
            ('BOW AND ARROW.opus', '01', 'BOW AND ARROW', 'Kenshi Yonezu')
        ]
    },
    'gg-20260920-140154': {
        'title': 'TV Anime "Sword Art Online Alternative Gun Gale Online II" OP Theme "GG"',
        'author': 'ReoNa',
        'disc': '0',
        'tracks': [
            ('GG.opus', '01', 'GG', 'ReoNa'),
            ('Watashitachi no uta.opus', '02', 'Watashitachi no uta', 'ReoNa'),
            ('Mosquito.opus', '03', 'Mosquito', 'ReoNa'),
            ('By myself.opus', '04', 'By myself', 'ReoNa'),
            ('GG -Instrumental-.opus', '05', 'GG -Instrumental-', 'ReoNa'),
            ('GG -TV size.opus', '06', 'GG -TV Size-', 'ReoNa')
        ]
    },
    'hello-to-goodbye-20260920-140154': {
        'title': 'TV Anime "Hitoribocchi no Isekai Kouryaku" ED Theme "Hello to Goodbye"',
        'author': 'Kujiragi',
        'disc': '0',
        'tracks': [
            ('Hangout.opus', '01', 'Hangout', 'Kujiragi'),
            ('Wonder Prologue.opus', '02', 'Wonder Prologue', 'Kujiragi'),
            ('Hello to Goodbye.opus', '03', 'Hello to Goodbye', 'Kujiragi')
        ]
    },
    'maou-2099-ost-1-20260920-140154': {
        'title': 'Maou 2099 Original Soundtrack Vol.1',
        'author': 'Kato Tatsuya',
        'disc': '0',
        'tracks': [
            ('The return of the king.opus', '01', 'The return of the king', 'Kato Tatsuya'),
            ('Fragile & Beauty.opus', '02', 'Fragile & Beauty', 'Kato Tatsuya'),
            ('Puzzled.opus', '03', 'Puzzled', 'Kato Tatsuya'),
            ('Life comes and goes.opus', '04', 'Life comes and goes', 'Kato Tatsuya'),
            ('Marcus.opus', '05', 'Marcus', 'Kato Tatsuya'),
            ('Absolute evil.opus', '06', 'Absolute evil', 'Kato Tatsuya'),
            ('Life is so bright.opus', '07', 'Life is so bright', 'Kato Tatsuya'),
            ('What a pretty.opus', '08', 'What a pretty', 'Kato Tatsuya'),
            ('Urban life.opus', '09', 'Urban life', 'Kato Tatsuya'),
            ('Goofy.opus', '10', 'Goofy', 'Kato Tatsuya'),
            ('SMH.opus', '11', 'SMH', 'Kato Tatsuya'),
            ('Wicked.opus', '12', 'Wicked', 'Kato Tatsuya'),
            ('Veltol Velvet Velsvalt.opus', '13', 'Veltol Velvet Velsvalt', 'Kato Tatsuya'),
            ('Back alley.opus', '14', 'Back alley', 'Kato Tatsuya'),
            ('The dominator.opus', '15', 'The dominator', 'Kato Tatsuya'),
            ('Seesaw battle.opus', '16', 'Seesaw battle', 'Kato Tatsuya'),
            ('Intelligence.opus', '17', 'Intelligence', 'Kato Tatsuya'),
            ('Make it snappy.opus', '18', 'Make it snappy', 'Kato Tatsuya'),
            ('Walking on eggshells.opus', '19', 'Walking on eggshells', 'Kato Tatsuya'),
            ('Hunting immortality.opus', '20', 'Hunting immortality', 'Kato Tatsuya'),
            ('Operation begins.opus', '21', 'Operation begins', 'Kato Tatsuya'),
            ('Maneuver.opus', '22', 'Maneuver', 'Kato Tatsuya'),
            ('Demon Lord 2099.opus', '23', 'Demon Lord 2099', 'Kato Tatsuya')
        ]
    },
    'under-blue-20260920-140154': {
        'title': 'Eve 4th Album "Under Blue"',
        'author': 'Eve',
        'disc': '0',
        'tracks': [
            ('Lazy Cat.opus', '01', 'Lazy Cat', 'Eve'),
            ('Teenage Blue.opus', '02', 'Teenage Blue', 'Eve'),
            ('Touhikou.opus', '03', 'Touhikou', 'Eve'),
            ('Kororon.opus', '04', 'Kororon', 'Eve'),
            ('FightSong.opus', '05', 'FightSong', 'Eve'),
            ('Hanaboshi.opus', '06', 'Hanaboshi', 'Eve'),
            ('Boukenroku.opus', '07', 'Boukenroku', 'Eve'),
            ('Byme.opus', '08', 'Byme', 'Eve'),
            ('The Rewind Story.opus', '09', 'The Rewind Story', 'Eve'),
            ('Insomnia.opus', '10', 'Insomnia', 'Eve'),
            ('Bubble feat.Uta.opus', '11', 'Bubble', 'Eve feat.Uta'),
            ('Sweet Memory.opus', '12', 'Sweet Memory', 'Eve'),
            ('Shirayuki.opus', '13', 'Shirayuki', 'Eve'),
            ('Midnight Runway.opus', '14', 'Midnight Runway', 'Eve'),
            ('Bokurano.opus', '15', 'Bokurano', 'Eve'),
            ('Hanaarashi.opus', '16', 'Hanaarashi', 'Eve'),
            ('Sayonara End Roll.opus', '17', 'Sayonara End Roll', 'Eve'),
            ('Under Blue.opus', '18', 'Under Blue', 'Eve'),
            ('Yumeni Aetara.opus', '19', 'Yumeni Aetara', 'Eve')
        ]
    },
    'wolpis-carter-20260920-140154': {
        'title': 'Korekaramo Wolpis-sha No Teikyou De Ookurishimasu',
        'author': 'Wolpis Carter',
        'disc': '0',
        'tracks': [
            ('Amanojaku.opus', '01', 'Amanojaku', 'Wolpis Carter'),
            ('Haikei Ni Tettou, Chizuru Wa Denen Nite Matsu..opus', '02', 'Haikei Ni Tettou, Chizuru Wa Denen Nite Matsu.', 'Wolpis Carter'),
            ('Justitia of Life.opus', '03', 'Justitia of Life', 'Wolpis Carter'),
            ('Streaming Heart.opus', '04', 'Streaming Heart', 'Wolpis Carter'),
            ('The Sun Goddess & Rat.opus', '05', 'The Sun Goddess & Rat', 'Wolpis Carter'),
            ('M.opus', '06', 'M', 'Wolpis Carter'),
            ('Orange.opus', '07', 'Orange', 'Wolpis Carter'),
            ('Kairai Mime.opus', '08', 'Kairai Mime', 'Wolpis Carter'),
            ('Miraiyosouzu II.opus', '09', 'Miraiyosouzu II', 'Wolpis Carter'),
            ('Deichu Ni Saku.opus', '10', 'Deichu Ni Saku', 'Wolpis Carter'),
            ('The Journey Home.opus', '11', 'THE JOURNEY HOME', 'Wolpis Carter')
        ]
    }
}

for folder_name, data in albums_data.items():
    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.exists(folder_path):
        print(f'Folder not found: {folder_path}')
        continue
    
    print(f'\n========================================')
    print(f'Processing: {folder_name}')
    
    flac_dir = os.path.join(folder_path, 'flac')
    
    authors_list = []
    titles_list = []
    
    for old_file, idx_str, title, artist in data['tracks']:
        authors_list.append(f'{idx_str} --- {artist}')
        titles_list.append(f'{idx_str} --- {title}')
        
        old_file_path = os.path.join(flac_dir, old_file)
        ext = os.path.splitext(old_file)[1]
        new_file_name = f'{idx_str}{ext}'
        new_file_path = os.path.join(flac_dir, new_file_name)
        
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f'  Renamed file: {old_file} -> {new_file_name}')
        elif os.path.exists(new_file_path):
            print(f'  File already named: {new_file_name}')
        else:
            print(f'  [!] File not found: {old_file}')

    here_data = {
        '1': authors_list,
        '2': [],
        '3': [],
        '4': [],
        'category': '2',
        'title': data['title'],
        'author': data['author'],
        'disc': data['disc'],
        'music_name_index': {
            '1': titles_list,
            '2': [],
            '3': [],
            '4': []
        },
        'id_category_list': {
            '1': 'IndoPride',
            '2': '日本の歌',
            '3': 'Jowo Mletre',
            '4': 'Worldwide',
            '5': 'Instrumental'
        },
        'source': 'discord'
    }
    
    here_path = os.path.join(folder_path, '.here.txt')
    with open(here_path, 'w', encoding='utf-8') as f:
        json.dump(here_data, f, indent=2, ensure_ascii=False)
    print(f'  Updated .here.txt successfully.')
    
    total_tracks = len(data['tracks'])
    new_folder_name = f'{total_tracks}-{folder_name}'
    new_folder_path = os.path.join(base_dir, new_folder_name)
    
    if folder_path != new_folder_path:
        os.rename(folder_path, new_folder_path)
        print(f'  Renamed folder: {folder_name} -> {new_folder_name}')

print('\nAll albums processed successfully!')
