import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    {
        'base_dir': r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\2-Anisong",
        'folder_name': 'one-piece-memorial-best-20260920-142613',
        'category': '2',
        'title': 'One Piece Memorial Best',
        'author': 'Various Artists',
        'disc': '2',
        'discs_tracks': {
            '1': [
                ('We Are!.opus', '01', 'We Are!', 'Kitadani Hiroshi'),
                ('Believe.opus', '02', 'Believe', 'Folder 5'),
                ('Toward the Light.opus', '03', 'Toward the Light', 'The BabyStars'),
                ('BON VOYAGE!.opus', '04', 'BON VOYAGE!', 'BON-BON BLANCO'),
                ('Map of the Human Heart.opus', '05', 'Map of the Human Heart', 'BOYSTYLE'),
                ('BRAND NEW WORLD.opus', '06', 'BRAND NEW WORLD', 'D-51'),
                ('We are 7 Straw-Hat Pirates.opus', '07', 'We are 7 Straw-Hat Pirates', 'Kitadani Hiroshi'),
                ('Crazy Rainbow.opus', '08', 'Crazy Rainbow', 'Tackey & Tsubasa'),
                ('Jungle P.opus', '09', 'Jungle P', '5050'),
                ('We Are One Piece 10th Anniversary.opus', '10', 'We Are One Piece 10th Anniversary', 'Tohoshinki'),
                ('Share The World.opus', '11', 'Share The World', 'Tohoshinki'),
                ('Looking for wind.opus', '12', 'Looking for wind', 'Yaguchi Mari'),
                ('memories.opus', '13', 'memories', 'Otsuki Maki'),
                ('RUN! RUN! RUN!.opus', '14', 'RUN! RUN! RUN!', 'Otsuki Maki'),
                ('I’m Here.opus', '15', 'I’m Here', 'TOMATO CUBE'),
                ('That’s a Fact.opus', '16', 'That’s a Fact', 'Suitei Shoujo')
            ],
            '2': [
                ('BEFORE DAWN.opus', '01', 'BEFORE DAWN', 'Ai-Sachi'),
                ('fish.opus', '02', 'fish', 'The Kaleidoscope'),
                ('GLORY -Since you’re here-.opus', '03', 'GLORY -Since you’re here-', 'Uehara Takako'),
                ('Shining ray.opus', '04', 'Shining ray', 'Janne Da Arc'),
                ('Free Will.opus', '05', 'Free Will', 'Ruppina'),
                ('FAITH.opus', '06', 'FAITH', 'Ruppina'),
                ('A to Z ～ONE PIECE Edition～.opus', '07', 'A to Z ～ONE PIECE Edition～', 'ZZ'),
                ('The moon and the sunflac.opus', '08', 'The moon and the sun', 'Shela'),
                ('DREAM SHIP.opus', '09', 'DREAM SHIP', 'Ikuta Aiko'),
                ('Future sailing.opus', '10', 'Future sailing', 'Tackey & Tsubasa'),
                ('Eternal Pose.opus', '11', 'Eternal Pose', 'ASIA ENGINEER'),
                ('Dear friends.opus', '12', 'Dear friends', 'TRIPLANE'),
                ('Because come tomorrow.opus', '13', 'Because come tomorrow', 'Tohoshinki'),
                ('ADVENTURE WORLD.opus', '14', 'ADVENTURE WORLD', 'Delicatessen'),
                ('Family.opus', '15', 'Family', 'Straw Hat Pirates'),
                ('Sake of Binks.opus', '16', 'Sake of Binks', 'Straw Hat Pirates'),
                ('A THOUSAND DREAMERS.opus', '17', 'A THOUSAND DREAMERS', 'Straw Hat Pirates')
            ]
        }
    },
    {
        'base_dir': r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\4-worldwide",
        'folder_name': 'plastic-hearts-20260920-142613',
        'category': '4',
        'title': 'Plastic Hearts',
        'author': 'Miley Cyrus',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('WTF Do I Know.opus', '01', 'WTF Do I Know', 'Miley Cyrus'),
                ('Plastic Hearts.opus', '02', 'Plastic Hearts', 'Miley Cyrus'),
                ('Angels Like You.opus', '03', 'Angels Like You', 'Miley Cyrus'),
                ('Prisoner (feat. Dua Lipa).opus', '04', 'Prisoner (feat. Dua Lipa)', 'Miley Cyrus feat. Dua Lipa'),
                ('Gimme What I Want.opus', '05', 'Gimme What I Want', 'Miley Cyrus'),
                ('Night Crawling (feat. Billy Idol).opus', '06', 'Night Crawling (feat. Billy Idol)', 'Miley Cyrus feat. Billy Idol'),
                ('Midnight Sky.opus', '07', 'Midnight Sky', 'Miley Cyrus'),
                ('High.opus', '08', 'High', 'Miley Cyrus'),
                ('Hate Me.opus', '09', 'Hate Me', 'Miley Cyrus'),
                ('Bad Karma (feat. Joan Jett).opus', '10', 'Bad Karma (feat. Joan Jett)', 'Miley Cyrus feat. Joan Jett'),
                ('Never Be Me.opus', '11', 'Never Be Me', 'Miley Cyrus'),
                ('Golden G String.opus', '12', 'Golden G String', 'Miley Cyrus'),
                ('Edge of Midnight (Midnight Sky Remix) [feat. Stevie Nicks].opus', '13', 'Edge of Midnight (Midnight Sky Remix) [feat. Stevie Nicks]', 'Miley Cyrus feat. Stevie Nicks'),
                ('Heart Of Glass (Live from the iHeart Festival).opus', '14', 'Heart Of Glass (Live from the iHeart Festival)', 'Miley Cyrus'),
                ('Zombie (Live from the NIVA Save Our Stages Festival).opus', '15', 'Zombie (Live from the NIVA Save Our Stages Festival)', 'Miley Cyrus')
            ]
        }
    },
    {
        'base_dir': r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\5-instrumental",
        'folder_name': 'edgerunners-ost-vol3-20260920-142613',
        'category': '5',
        'title': 'Cyberpunk: Edgerunners Soundtrack Vol.3 (Ep5+6)',
        'author': 'Various Artists',
        'disc': '0',
        'discs_tracks': {
            'flac': [
                ('Nie Pytaj Nas.opus', '01', 'Nie Pytaj Nas', 'Zjednoczenie Soundsystem'),
                ('I Will Follow.opus', '02', 'I Will Follow', 'Snot Abundance'),
                ('Dom.opus', '03', 'Dom', 'Zjednoczenie Soundsystem feat. Damian Syjonfam'),
                ('Undertow Velocity.opus', '04', 'Undertow Velocity', 'Private Press'),
                ('The Voice in My Head.opus', '05', 'The Voice in My Head', 'P.T. Adamczyk'),
                ('Cyberwildlife Park.opus', '06', 'Cyberwildlife Park', 'Marcin Przybylowicz'),
                ('Modern Anthill.opus', '07', 'Modern Anthill', 'Marcin Przybylowicz'),
                ('Health.opus', '08', 'Health', 'Major Crimes'),
                ('Consumer Cathedral.opus', '09', 'Consumer Cathedral', 'Marcin Przybylowicz'),
                ('1101 Break.opus', '10', '1101 Break', 'Private Press'),
                ('Fuelled by Poison.opus', '11', 'Fuelled by Poison', 'Antigama'),
                ('Juiced Up.opus', '12', 'Juiced Up', 'P.T. Adamczyk'),
                ('Żurawie.opus', '13', 'Żurawie', 'Ugory')
            ]
        }
    },
    {
        'base_dir': r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\5-instrumental",
        'folder_name': 'tog-the-return-of-the-prince-ost-20260920-142613',
        'category': '5',
        'title': 'TV Anime "Kami no Tou -Tower of God- The Return of the Prince" Original Soundtrack',
        'author': 'Kevin Penkin, Various Artists',
        'disc': '2',
        'discs_tracks': {
            '1': [
                ('Viole.opus', '01', 'Viole', 'Kevin Penkin'),
                ('Brute.opus', '02', 'Brute', 'Kevin Penkin'),
                ('Night the FUG.opus', '03', 'Night the FUG', 'Kevin Penkin'),
                ('The Zahard Kingdom.opus', '04', 'The Zahard Kingdom', 'Kevin Penkin'),
                ('FUG Yu.opus', '05', 'FUG Yu', 'Kevin Penkin'),
                ('Abyssal Rachel.opus', '06', 'Abyssal Rachel', 'Kevin Penkin'),
                ('Mark XX.opus', '07', 'Mark XX', 'Kevin Penkin'),
                ('Changes.opus', '08', 'Changes', 'Kevin Penkin'),
                ('ROTAS.opus', '09', 'ROTAS', 'Kevin Penkin'),
                ('Stars II.opus', '10', 'Stars II', 'Kevin Penkin'),
                ('Room of Belief [ROOM].opus', '11', 'Room of Belief [ROOM]', 'Kevin Penkin'),
                ('Viole Runs.opus', '12', 'Viole Runs', 'Kevin Penkin & James Landino'),
                ('Letter.opus', '13', 'Letter', 'Kevin Penkin'),
                ('Song.opus', '14', 'Song', 'Kevin Penkin'),
                ('Irreplaceable Things.opus', '15', 'Irreplaceable Things', 'Kevin Penkin'),
                ('Ascension.opus', '16', 'Ascension', 'feeding ear & Kevin Penkin')
            ],
            '2': [
                ('Emblem of FUG.opus', '01', 'Emblem of FUG', 'Nakamura Yoshiki'),
                ('Wangan Advances.opus', '02', 'Wangan Advances', 'Fukuba Yosuke'),
                ('Urek Mazino.opus', '03', 'Urek Mazino', 'Fukuba Yosuke'),
                ('The Trustworthy Room.opus', '04', 'The Trustworthy Room', 'Fujimaki Hiroshi'),
                ('Out of Bounds.opus', '05', 'Out of Bounds', 'Nakamura Yoshiki'),
                ('Rapdevil.opus', '06', 'Rapdevil', 'Nakamura Yoshiki'),
                ('The Mighty Fighter.opus', '07', 'The Mighty Fighter', 'Fujimaki Hiroshi'),
                ('Domination.opus', '08', 'Domination', 'Takahashi Tetsuya'),
                ('Unexpected Proposal.opus', '09', 'Unexpected Proposal', 'Takahashi Tetsuya'),
                ('Stagnation.opus', '10', 'Stagnation', 'Morohashi Kuniyuki'),
                ('Revenge.opus', '11', 'Revenge', 'Morohashi Kuniyuki'),
                ('Yeon Yihwa.opus', '12', 'Yeon Yihwa', 'Inukai Kanade'),
                ('Hwa Ryun.opus', '13', 'Hwa Ryun', 'Inukai Kanade'),
                ('Ilmar & Cassano.opus', '14', 'Ilmar & Cassano', 'Inukai Kanade'),
                ('The Hand of Arlen.opus', '15', 'The Hand of Arlen', 'Inukai Kanade'),
                ('One Opportunity.opus', '16', 'One Opportunity', 'Inukai Kanade'),
                ('Starting Weapon.opus', '17', 'Starting Weapon', 'Inukai Kanade'),
                ('Battlefront.opus', '18', 'Battlefront', 'Inukai Kanade'),
                ('Challenger.opus', '19', 'Challenger', 'Inukai Kanade'),
                ('Suspicion.opus', '20', 'Suspicion', 'Inukai Kanade'),
                ('Dirty Trick.opus', '21', 'Dirty Trick', 'Inukai Kanade'),
                ('Lighthearted Layers.opus', '22', 'Lighthearted Layers', 'BeauDamian'),
                ('Golden Days.opus', '23', 'Golden Days', 'BeauDamian'),
                ('Flawed Foe.opus', '24', 'Flawed Foe', 'BeauDamian'),
                ('Silly Shenanigans.opus', '25', 'Silly Shenanigans', 'BeauDamian')
            ]
        }
    },
    {
        'base_dir': r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD\5-instrumental",
        'folder_name': 'tog-workshop-battle-ost-20260920-142613',
        'category': '5',
        'title': 'TV Anime "Kami no Tou -Tower of God- Workshop Battle" Original Soundtrack',
        'author': 'Kevin Penkin, Various Artists',
        'disc': '2',
        'discs_tracks': {
            '1': [
                ('Water Stadium.opus', '01', 'Water Stadium', 'Kevin Penkin'),
                ('Quant’s Moonwind Pie.opus', '02', 'Quant’s Moonwind Pie', 'Kevin Penkin'),
                ('Thornrose.opus', '03', 'Thornrose', 'Kevin Penkin'),
                ('Meditations on Heads Stuck in a Jar.opus', '04', 'Meditations on Heads Stuck in a Jar', 'Kevin Penkin'),
                ('The Unknown.opus', '05', 'The Unknown', 'Kevin Penkin'),
                ('Exceeding Assumptions.opus', '06', 'Exceeding Assumptions', 'Kevin Penkin & feeding ear'),
                ('Crow.opus', '07', 'Crow', 'Kevin Penkin'),
                ('Megaladon.opus', '08', 'Megaladon', 'Kevin Penkin'),
                ('Room of Belief [BATTLE].opus', '09', 'Room of Belief [BATTLE]', 'Kevin Penkin'),
                ('Niki.opus', '10', 'Niki', 'Kevin Penkin'),
                ('Hoynes.opus', '11', 'Hoynes', 'Kevin Penkin'),
                ('Brainbed.opus', '12', 'Brainbed', 'Kevin Penkin'),
                ('Viole the Berserker.opus', '13', 'Viole the Berserker', 'Kevin Penkin'),
                ('String Theory.opus', '14', 'String Theory', 'Kevin Penkin'),
                ('Become the God.opus', '15', 'Become the God', 'Kevin Penkin'),
                ('Viole Appears.opus', '16', 'Viole Appears', 'Kevin Penkin')
            ],
            '2': [
                ('Mad Dog.opus', '01', 'Mad Dog', 'Fukuba Yosuke'),
                ('Beta.opus', '02', 'Beta', 'Nakamura Yoshiki'),
                ('Archimedes.opus', '03', 'Archimedes', 'Takahashi Tetsuya'),
                ('Rush.opus', '04', 'Rush', 'Nakamura Yoshiki'),
                ('Barely Alive.opus', '05', 'Barely Alive', 'Nakamura Yoshiki'),
                ('Close Quarters Combat.opus', '06', 'Close Quarters Combat', 'Fujimaki Hiroshi'),
                ('Out of Control.opus', '07', 'Out of Control', 'Fukuba Yosuke'),
                ('Go Forward.opus', '08', 'Go Forward', 'Takahashi Tetsuya'),
                ('Joyful Moment.opus', '09', 'Joyful Moment', 'Fukuba Yosuke'),
                ('Lost Vigilance.opus', '10', 'Lost Vigilance', 'Morohashi Kuniyuki'),
                ('EMILE.opus', '11', 'EMILE', 'Inukai Kanade'),
                ('Negligence.opus', '12', 'Negligence', 'Inukai Kanade'),
                ('Escape.opus', '13', 'Escape', 'Inukai Kanade'),
                ('Turning Fates.opus', '14', 'Turning Fates', 'Inukai Kanade'),
                ('Ranker Battle.opus', '15', 'Ranker Battle', 'Inukai Kanade'),
                ('Tactics.opus', '16', 'Tactics', 'Inukai Kanade'),
                ('EMILE (Truth).opus', '17', 'EMILE (Truth)', 'Inukai Kanade'),
                ('Unconvincing Proposal.opus', '18', 'Unconvincing Proposal', 'Inukai Kanade'),
                ('Operation.opus', '19', 'Operation', 'Inukai Kanade'),
                ('Unnatural.opus', '20', 'Unnatural', 'Inukai Kanade'),
                ('Rushed by Fate.opus', '21', 'Rushed by Fate', 'BeauDamian'),
                ('Speed Striker.opus', '22', 'Speed Striker', 'BeauDamian'),
                ('Run for Giggles.opus', '23', 'Run for Giggles', 'BeauDamian'),
                ('Till the Break of Dawn.opus', '24', 'Till the Break of Dawn', 'BeauDamian')
            ]
        }
    }
]

for task in tasks:
    base_dir = task['base_dir']
    folder_name = task['folder_name']
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
        'category': task['category'],
        'title': task['title'],
        'author': task['author'],
        'disc': task['disc'],
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
    
    for subfolder_key, tracks_list in task['discs_tracks'].items():
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

print("\nAll batch albums processed successfully!")
