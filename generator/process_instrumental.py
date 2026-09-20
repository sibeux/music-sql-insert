import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\5-instrumental"

albums_data = {
    'cyberpunk-edgerunners-20260920-141358': {
        'title': 'Cyberpunk: Edgerunners (Original Series Soundtrack)',
        'author': 'Akira Yamaoka, Marcin Przybylowicz, P.T. Adamczyk',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('This Fffire.opus', '01', 'This Fffire', 'Franz Ferdinand'),
                ('Opening Credits.opus', '02', 'Opening Credits', 'Akira Yamaoka'),
                ('Modern Anthill.opus', '03', 'Modern Anthill', 'Marcin Przybylowicz'),
                ('Sudden Skirmish.opus', '04', 'Sudden Skirmish', 'Akira Yamaoka'),
                ('Like a Boy.opus', '05', 'Like a Boy', 'Akira Yamaoka'),
                ('Cloudy Day.opus', '06', 'Cloudy Day', 'Marcin Przybylowicz'),
                ('Whatever It Takes.opus', '07', 'Whatever It Takes', 'Akira Yamaoka'),
                ('Into the Fire.opus', '08', 'Into the Fire', 'Akira Yamaoka'),
                ('Consumer Cathedral.opus', '09', 'Consumer Cathedral', 'Marcin Przybylowicz'),
                ('Juiced Up.opus', '10', 'Juiced Up', 'P.T. Adamczyk'),
                ('Lucky You.opus', '11', 'Lucky You', 'Akira Yamaoka'),
                ('Whatever Choom, Like I Give a Sht.opus', '12', 'Whatever Choom, Like I Give a Sht', 'Akira Yamaoka'),
                ('Run to the Edge.opus', '13', 'Run to the Edge', 'Marcin Przybylowicz & P.T. Adamczyk'),
                ('Let You Down.opus', '14', 'Let You Down', 'Dawid Podsiadlo')
            ]
        }
    },
    'dandadan-ost-20260920-141358': {
        'title': 'TV Anime "Dandadan" Original Soundtrack',
        'author': 'Ushio Kensuke',
        'disc': '2',
        'discs_tracks': {
            '1': [
                ('code ⁚ DDD.opus', '01', 'code : DDD', 'Ushio Kensuke'),
                ('a slice of peach.opus', '02', 'a slice of peach', 'Ushio Kensuke'),
                ('okarun’s file.opus', '03', "okarun's file", 'Ushio Kensuke'),
                ('tiger and flower.opus', '04', 'tiger and flower', 'Ushio Kensuke'),
                ('seiko.opus', '05', 'seiko', 'Ushio Kensuke'),
                ('serpoians.opus', '06', 'serpoians', 'Ushio Kensuke'),
                ('supernatural power.opus', '07', 'supernatural power', 'Ushio Kensuke'),
                ('(un)lucky cat.opus', '08', '(un)lucky cat', 'Ushio Kensuke'),
                ('code ⁚ DDD(Ver.H).opus', '09', 'code : DDD(Ver.H)', 'Ushio Kensuke'),
                ('on the edge.opus', '10', 'on the edge', 'Ushio Kensuke'),
                ('like a fire.opus', '11', 'like a fire', 'Ushio Kensuke'),
                ('william hell overture.opus', '12', 'william hell overture', 'Ushio Kensuke'),
                ('paranormal funk.opus', '13', 'paranormal funk', 'Ushio Kensuke'),
                ('breakthrough.opus', '14', 'breakthrough', 'Ushio Kensuke'),
                ('the tunnel.opus', '15', 'the tunnel', 'Ushio Kensuke'),
                ('the girls.opus', '16', 'the girls', 'Ushio Kensuke'),
                ('turbo granny.opus', '17', 'turbo granny', 'Ushio Kensuke')
            ],
            '2': [
                ('momo.opus', '01', 'momo', 'Ushio Kensuke'),
                ('okarun’s life.opus', '02', "okarun's life", 'Ushio Kensuke'),
                ('more than friends.opus', '03', 'more than friends', 'Ushio Kensuke'),
                ('less than lovers.opus', '04', 'less than lovers', 'Ushio Kensuke'),
                ('aira.opus', '05', 'aira', 'Ushio Kensuke'),
                ('can’t take it anymore!!.opus', '06', "can't take it anymore!!", 'Ushio Kensuke'),
                ('the briefing.opus', '07', 'the briefing', 'Ushio Kensuke'),
                ('the crawling ghost.opus', '08', 'the crawling ghost', 'Ushio Kensuke'),
                ('curse.opus', '09', 'curse', 'Ushio Kensuke'),
                ('love theme.opus', '10', 'love theme', 'Ushio Kensuke'),
                ('acrobatic silky.opus', '11', 'acrobatic silky', 'Ushio Kensuke'),
                ('code ⁚ DDD(Ver.O).opus', '12', 'code : DDD(Ver.O)', 'Ushio Kensuke'),
                ('jiji!.opus', '13', 'jiji!', 'Ushio Kensuke'),
                ('spoken spell.opus', '14', 'spoken spell', 'Ushio Kensuke'),
                ('taro and hanako.opus', '15', 'taro and hanako', 'Ushio Kensuke'),
                ('the kitos.opus', '16', 'the kitos', 'Ushio Kensuke')
            ]
        }
    },
    'negaposi-ost-3-20260920-141358': {
        'title': 'TV Anime "NegaPosi Angler" Original Soundtrack #3',
        'author': 'Tomoki Kikuya',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('Life Is Not Easy.opus', '01', 'Life Is Not Easy', 'Tomoki Kikuya'),
                ('All I Can Do Is Run Away.opus', '02', 'All I Can Do Is Run Away', 'Tomoki Kikuya'),
                ('Cat.opus', '03', 'Cat', 'Tomoki Kikuya'),
                ('Triakis Scyllium.opus', '04', 'Triakis Scyllium', 'Tomoki Kikuya'),
                ('Omatsuri.opus', '05', 'Omatsuri', 'Tomoki Kikuya'),
                ('Split the Winnings.opus', '06', 'Split the Winnings', 'Tomoki Kikuya'),
                ('Move.opus', '07', 'Move', 'Tomoki Kikuya'),
                ('Easygoing.opus', '08', 'Easygoing', 'Tomoki Kikuya'),
                ('What Is the Million Yen For.opus', '09', 'What Is the Million Yen For?', 'Tomoki Kikuya'),
                ('Wait!.opus', '10', 'Wait!', 'Tomoki Kikuya'),
                ('Can We Start Over.opus', '11', 'Can We Start Over?', 'Tomoki Kikuya'),
                ('Stingray.opus', '12', 'Stingray', 'Tomoki Kikuya'),
                ('Roommates.opus', '13', 'Roommates', 'Tomoki Kikuya')
            ]
        }
    },
    'negaposi-ost-4-20260920-141358': {
        'title': 'TV Anime "NegaPosi Angler" Original Soundtrack #4',
        'author': 'Tomoki Kikuya',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('This Convenience Store Is Weird.opus', '01', 'This Convenience Store Is Weird', 'Tomoki Kikuya'),
                ('I Don’ Know at All.opus', '02', "I Don' Know at All", 'Tomoki Kikuya'),
                ('Cute Lure.opus', '03', 'Cute Lure', 'Tomoki Kikuya'),
                ('38 Oz.opus', '04', '3/8 Oz', 'Tomoki Kikuya'),
                ('Maniacal Angler.opus', '05', 'Maniacal Angler', 'Tomoki Kikuya'),
                ('Breakdown.opus', '06', 'Breakdown', 'Tomoki Kikuya'),
                ('O-Tsuri.opus', '07', 'O-Tsuri', 'Tomoki Kikuya'),
                ('New Fishing Goods.opus', '08', 'New Fishing Goods', 'Tomoki Kikuya'),
                ('What Do You Mean.opus', '09', 'What Do You Mean?', 'Tomoki Kikuya'),
                ('Days of Hana.opus', '10', 'Days of Hana', 'Tomoki Kikuya'),
                ('What Is a Lure.opus', '11', 'What Is a Lure?', 'Tomoki Kikuya'),
                ('Reeling.opus', '12', 'Reeling', 'Tomoki Kikuya'),
                ('Far Away.opus', '13', 'Far Away', 'Tomoki Kikuya'),
                ('Hana’s House.opus', '14', "Hana's House", 'Tomoki Kikuya'),
                ('Sea Bass.opus', '15', 'Sea Bass', 'Tomoki Kikuya'),
                ('Oh, Tsuri....opus', '16', 'Oh, Tsuri...', 'Tomoki Kikuya')
            ]
        }
    },
    'negaposi-ost-5-20260920-141358': {
        'title': 'TV Anime "NegaPosi Angler" Original Soundtrack #5',
        'author': 'Tomoki Kikuya',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('Job Done.opus', '01', 'Job Done', 'Tomoki Kikuya'),
                ('No Dream No Life.opus', '02', 'No Dream No Life', 'Tomoki Kikuya'),
                ('Oh My God.opus', '03', 'Oh My God', 'Tomoki Kikuya'),
                ('Fishing Tackle Store.opus', '04', 'Fishing Tackle Store', 'Tomoki Kikuya'),
                ('Would You Date Me.opus', '05', 'Would You Date Me?', 'Tomoki Kikuya'),
                ('No Money No Life.opus', '06', 'No Money No Life', 'Tomoki Kikuya'),
                ('Date.opus', '07', 'Date', 'Tomoki Kikuya'),
                ('Sometimes People Make Mistakes.opus', '08', 'Sometimes People Make Mistakes', 'Tomoki Kikuya'),
                ('Float Fishing.opus', '09', 'Float Fishing', 'Tomoki Kikuya'),
                ('Do You Like It.opus', '10', 'Do You Like It?', 'Tomoki Kikuya'),
                ('Let’s Have Dinner Together.opus', '11', "Let's Have Dinner Together", 'Tomoki Kikuya'),
                ('Hit Again.opus', '12', 'Hit Again', 'Tomoki Kikuya'),
                ('Sunset.opus', '13', 'Sunset', 'Tomoki Kikuya'),
                ('Mr. Fujishiro.opus', '14', 'Mr. Fujishiro', 'Tomoki Kikuya'),
                ('Be Honest with Yourself.opus', '15', 'Be Honest with Yourself', 'Tomoki Kikuya'),
                ('Sometimes People Make Mistakes #2.opus', '16', 'Sometimes People Make Mistakes #2', 'Tomoki Kikuya'),
                ('Nice Aiming.opus', '17', 'Nice Aiming', 'Tomoki Kikuya'),
                ('Sometimes People Make Mistakes #3.opus', '18', 'Sometimes People Make Mistakes #3', 'Tomoki Kikuya')
            ]
        }
    },
    'negaposi-ost-10-20260920-141358': {
        'title': 'TV Anime "NegaPosi Angler" Original Soundtrack #10',
        'author': 'Tomoki Kikuya',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('HOSPITAL.opus', '01', 'HOSPITAL', 'Tomoki Kikuya'),
                ('TWO YEARS.opus', '02', 'TWO YEARS', 'Tomoki Kikuya'),
                ('NEGATIVE.opus', '03', 'NEGATIVE', 'Tomoki Kikuya'),
                ('RANKER.opus', '04', 'RANKER', 'Tomoki Kikuya'),
                ('TAKE IT EASY.opus', '05', 'TAKE IT EASY', 'Tomoki Kikuya'),
                ('IT WAS A BIG ONE.opus', '06', 'IT WAS A BIG ONE', 'Tomoki Kikuya'),
                ('DON’T GO IT ALONE.opus', '07', "DON'T GO IT ALONE", 'Tomoki Kikuya'),
                ('KINDNESS IN HIS WAY.opus', '08', 'KINDNESS IN HIS WAY', 'Tomoki Kikuya'),
                ('THE HIDDEN PAST.opus', '09', 'THE HIDDEN PAST', 'Tomoki Kikuya'),
                ('I DIDN’T KNOW ANYTHING ABOUT YOU.opus', '10', "I DIDN'T KNOW ANYTHING ABOUT YOU", 'Tomoki Kikuya'),
                ('PROMISE.opus', '11', 'PROMISE', 'Tomoki Kikuya'),
                ('SILENT ANGER.opus', '12', 'SILENT ANGER', 'Tomoki Kikuya'),
                ('I’M SCARED.opus', '13', "I'M SCARED", 'Tomoki Kikuya')
            ]
        }
    }
}

for folder_name, data in albums_data.items():
    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        continue
    
    print(f"\n========================================")
    print(f"Processing: {folder_name}")
    
    here_data = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        'category': '2',
        'title': data['title'],
        'author': data['author'],
        'disc': data['disc'],
        'music_name_index': {
            '1': [],
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
    
    total_tracks = 0
    
    for subfolder_key, tracks_list in data['discs_tracks'].items():
        disc_num_key = '1' if subfolder_key == 'flac' else subfolder_key
        sub_dir = os.path.join(folder_path, subfolder_key)
        
        for old_file, idx_str, title, artist in tracks_list:
            total_tracks += 1
            here_data[disc_num_key].append(f"{idx_str} --- {artist}")
            here_data['music_name_index'][disc_num_key].append(f"{idx_str} --- {title}")
            
            old_file_path = os.path.join(sub_dir, old_file)
            ext = os.path.splitext(old_file)[1]
            new_file_name = f"{idx_str}{ext}"
            new_file_path = os.path.join(sub_dir, new_file_name)
            
            if os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)
                print(f"  [{subfolder_key}] Renamed file: {old_file} -> {new_file_name}")
            elif os.path.exists(new_file_path):
                print(f"  [{subfolder_key}] File already named: {new_file_name}")
            else:
                print(f"  [{subfolder_key}] [!] File not found: {old_file}")
                
    here_path = os.path.join(folder_path, '.here.txt')
    with open(here_path, 'w', encoding='utf-8') as f:
        json.dump(here_data, f, indent=2, ensure_ascii=False)
    print(f"  Updated .here.txt successfully.")
    
    new_folder_name = f"{total_tracks}-{folder_name}"
    new_folder_path = os.path.join(base_dir, new_folder_name)
    
    if folder_path != new_folder_path:
        os.rename(folder_path, new_folder_path)
        print(f"  Renamed folder: {folder_name} -> {new_folder_name}")

print("\nAll instrumental albums processed successfully!")
