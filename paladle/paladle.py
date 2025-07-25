import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from betterplaysound import playsound
import requests
#import tempfile
from importlib.resources import files, as_file
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import argparse
import sys


def main():
    champions = ['Androxus', 'Ash', 'Atlas', 'Azaan', 'Barik', 'Betty', 'Bomb King', 'Buck', 'Caspian', 'Cassie', 'Corvus', 'Dredge', 'Drogoz', 'Evie',
                 'Fernando', 'Furia', 'Grohk', 'Grover', 'Imani', 'Inara', 'Io', 'Jenos', 'Kasumi', 'Khan', 'Kinessa', 'Koga', 'Lex', 'Lian', 'Lillith',
                 'Maeve', 'Makoa', "Mal'Damba", 'Moji', 'Nyx', 'Octavia', 'Omen', 'Pip', 'Raum', 'Rei', 'Ruckus', 'Saati', 'Seris', 'Sha Lin', 'Skye', 'Strix',
                 'Talus', 'Terminus', 'Tiberius', 'Torvald', 'Tyra', 'VII', 'Vatu', 'Viktor', 'Vivian', 'Vora', 'Willo', 'Yagorath', 'Ying', 'Zhin']


    parser = argparse.ArgumentParser(description='Modify how you play Paladle')
    parser.add_argument('-u', action='store_true', help='Lets you only play the Ult Voice Line (text) category')
    parser.add_argument('-q', action='store_true', help='Lets you only play the Voice Line (audio) category')
    parser.add_argument('-a', action='store_true', help='Lets you only play the Ability category')
    parser.add_argument('-v', action='store_true', help='Lets you only play the VGS category')
    parser.add_argument('-t', action='store_true', help='Lets you only play the Talent category')
    parser.add_argument('-l', action='store_true', help='Lets you loop the game without having to start it manually again. '
                                                        'Use Ctrl + c to exit out of the game.') #May be combined with one other command line option. e.g. --la

    args = parser.parse_args()
    argused = True

    if args.u:
        guess_the_ult_voiceline_text(champions, argused)
    elif args.q:
        guess_the_voiceline_sound(champions, argused)
    elif args.a:
        guess_the_ability(champions, argused)
    elif args.v:
        guess_vgs_keys(argused)
    elif args.t:
        guess_talent(champions, argused)
    else:
        pass

    '''
    if loopcheck == True:
        pass
    else:
    '''
    print(f'Welcome to {Fore.CYAN}Paladle!{Style.RESET_ALL}\n')

    argused = False
    vcheck()
    guess_the_ult_voiceline_text(champions, argused)
    guess_the_voiceline_sound(champions, argused)
    guess_the_ability(champions, argused)
    guess_vgs_keys(argused)
    if args.l:
        loop = True
        guess_talent(champions, argused, loop)
    else:
        loop = False
        guess_talent(champions, argused, loop)

def vcheck():
    v_file = files('paladle').joinpath('vcheck')
    with open(v_file, 'r', encoding='utf-8') as f:
        v = f.read()

    remote_v_file = 'https://raw.githubusercontent.com/lulkaorg/paladle/refs/heads/main/paladle/vcheck'
    response = requests.get(remote_v_file)
    if response.status_code == 200:
        remote_v = response.text

    else:
        pass


    if v != remote_v:
        print(f'{Fore.RED}New update for Paladle is available!\nFollow the instructions on how to update here:{Style.RESET_ALL} '
              f'{Fore.BLUE}https://github.com/lulkaorg/paladle/tree/main?tab=readme-ov-file#updating{Style.RESET_ALL}\n')

    else:
        pass


def guess_the_ult_voiceline_text(champions, argused):
    random_champion = random.choice(champions)
    #champ_file = open(f'voicelines_text/{random_champion}', 'r')
    #content = champ_file.read()
    #print(content)
    #champ_file.close()
    champ_file = files('paladle.voicelines_text').joinpath(random_champion)
    with open(champ_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)


    guess = input('Which champions ult voice lines are these? ')
    i = 0
    hint = random_champion[0]

    while guess != random_champion:
        print(f'{Fore.RED}Wrong!{Style.RESET_ALL}')
        if i == 4:
            print(f'Hint: The champions name starts with {hint}')
            i = 0
        else:
            i += 1
        guess = input('Try again: ')

    if guess == random_champion:
        print(f'{Fore.GREEN}Correct!{Style.RESET_ALL}\n')

        if argused == True:
            sys.exit()

def guess_the_ability(champions, argused):
    random_champion = random.choice(champions)
    #champ_file = open(f'ability_names/{random_champion}', 'r')
    #content = champ_file.read().splitlines()
    #random_line = random.choice(content)
    #print(random_line)
    #champ_file.close()
    champ_file = files('paladle.ability_names').joinpath(random_champion)
    with open(champ_file, 'r', encoding='utf-8') as f:
        content = f.read().splitlines()
        random_line = random.choice(content)
        print(random_line)

    guess = input('Which champion is this ability/weapon name from? ')
    i = 0
    hint = random_champion[0]

    while guess != random_champion:
        print(f'{Fore.RED}Wrong!{Style.RESET_ALL}')
        if i == 4:
            print(f'Hint: The champions name starts with {hint}')
            i = 0
        else:
            i += 1
        guess = input('Try again: ')

    if guess == random_champion:
        print(f'{Fore.GREEN}Correct!{Style.RESET_ALL}\n')

        if argused == True:
            sys.exit()

def guess_the_voiceline_sound(champions, argused):
    on_or_off = int(input('Guess the Champion by a voice line.\nPlay the audio file from an online source or offline?\n'
                          'Online(0) or Offline(1): '))

    if on_or_off == 1:
        random_champion = random.choice(champions)
        #all_voice_files = [f for f in os.listdir(f'voicelines_audio/{random_champion}') if os.path.isfile(os.path.join(f'voicelines_audio/{random_champion}', f))]
        #random_voice_file = random.choice(all_voice_files)
        #playsound(f'voicelines_audio/{random_champion}/{random_voice_file}')
        all_voice_files = files('paladle.voicelines_audio').joinpath(random_champion)
        with as_file(all_voice_files) as dir_path:
            all_voice_files = [
                f for f in os.listdir(dir_path)
                if os.path.isfile(dir_path / f)
            ]
            random_voice_file = random.choice(all_voice_files)
            full_path = dir_path / random_voice_file
            playsound(str(full_path))

        guess = input('Which champion is this voice line from? ')
        i = 0
        hint = random_champion[0]

        while guess != random_champion:
            print(f'{Fore.RED}Wrong!{Style.RESET_ALL}')
            if i == 4:
                print(f'Hint: The champions name starts with {hint}')
                #playsound(f'voicelines_audio/{random_champion}/{random_voice_file}')
                playsound(str(full_path))
                i = 0
            else:
                i += 1
            guess = input('Try again: ')

        if guess == random_champion:
            print(f'{Fore.GREEN}Correct!{Style.RESET_ALL}\n')

            if argused == True:
                sys.exit()

    elif on_or_off == 0:
        print(f'{Fore.RED}Coming soon! Please select "Offline" (1) for now.{Style.RESET_ALL}\n')

        if argused == False:
            argused = False
            guess_the_voiceline_sound(champions, argused)

        elif argused == True:
            argused = True
            guess_the_voiceline_sound(champions, argused)

    else:
        print(f'{Fore.RED}Invalid input. Enter "0" for online or "1" for offline.{Style.RESET_ALL}\n')

        if argused == False:
            argused = False
            guess_the_voiceline_sound(champions, argused)

        elif argused == True:
            argused = True
            guess_the_voiceline_sound(champions, argused)


def guess_vgs_keys(argused):
    answer = input('"legacy" VGS or "new" VGS? ')

    while answer == 'legacy':
        print('Coming soon! (Maybe)')
        answer = input('"legacy" VGS or "new" VGS? ')

    if answer == 'new':
        z_vvf1 = {'vvf1': "Flank left!"}
        z_vvf2 = {'vvf2': "Attack up the middle!"}
        z_vvf3 = {'vvf3': "Flank right!"}
        z_vvff = {'vvff': "Attack!"}
        vvf = [z_vvf1, z_vvf2, z_vvf3, z_vvff]

        z_vvr1 = {'vvr1': "Enemies on the left flank!"}
        z_vvr2 = {'vvr2': "Enemies up the middle!"}
        z_vvr3 = {'vvr3': "Enemies on the right flank!"}
        z_vvrr = {'vvrr': "Enemies on the point!"}
        vvr = [z_vvr1, z_vvr2, z_vvr3, z_vvrr]

        z_vve1 = {'vve1': "I'll attack left flank!"}
        z_vve2 = {'vve2': "I'll attack up the middle!"}
        z_vve3 = {'vve3': "I'll attack right flank!"}
        z_vvee = {'vvee': "I'll attack!"}
        vve = [z_vve1, z_vve2, z_vve3, z_vvee]

        z_vvq1 = {'vvq1': "Defend left flank!"}
        z_vvq2 = {'vvq2': "Defend the middle!"}
        z_vvq3 = {'vvq3': "Defend right flank!"}
        z_vvqq = {'vvqq': "Defend!"}
        vvq = [z_vvq1, z_vvq2, z_vvq3, z_vvqq]

        z_vgq = {'vgq': "Spread out!"}
        z_vge = {'vge': "Wait!"}
        z_vgr = {'vgr': "Be careful!"}
        z_vgf = {'vgf': "Retreat!"}
        vg = [z_vgq, z_vge, z_vgr, z_vgf]


        z_vbq = {'vbq': "Enemies behind us!"}
        z_vbe = {'vbe': "Chase the enemy!"}
        z_vbr = {'vbr': "On my way!"}
        z_vbf = {'vbf': "I´m on it!"}
        vb = [z_vbq, z_vbe, z_vbr, z_vbf]

        z_vcfq = {'vcfq': 'I´m the greatest!'}
        z_vcfe = {'vcfe': "You rock!"}
        z_vcfr = {'vcfr': "Thanks!"}
        z_vcff = {'vcff': "No problem!"}
        vcf = [z_vcfq, z_vcfe, z_vcfr, z_vcff]

        z_vcrq = {'vcrq': 'Yes!'}
        z_vcre = {'vcre': 'No!'}
        z_vcrr = {'vcrr': 'Okay!'}
        z_vcrf = {'vcrf': 'Cancel that!'}
        vcr = [z_vcrq, z_vcre, z_vcrr, z_vcrf]

        z_vceq = {'vceq': 'Oops!'}
        z_vcee = {'vcee': 'Awesome! / Woohoo!'}
        z_vcer = {'vcer': 'Curses! / That´s too bad!'}
        z_vcef = {'vcef': 'Sorry'}
        vce = [z_vceq, z_vcee, z_vcer, z_vcef]

        z_vcqq = {'vcqq': 'Good luck! / Have fun!'}
        z_vcqe = {'vcqe': 'Good game!'}
        z_vcqr = {'vcqr': 'Hi!'}
        z_vcqf = {'vcqf': 'Completed!'}
        vcq = [z_vcqq, z_vcqe, z_vcqr, z_vcqf]

        z_vq = {'vq': 'Attack the Objective! / Contest the Objective!'}
        z_ve = {'ve': 'Help! / Need Healing!'}
        z_vr = {'vr': 'Ultimate is down! / Ultimate is ready!'}
        z_vf = {'vf': 'Group up!'}
        v = [z_vq, z_ve, z_vr, z_vf]

        random_vgs_voice_line = random.choice(v + vcq + vce + vcr + vcf + vb + vg + vvq + vve + vvr + vvf)
        print(*random_vgs_voice_line.values())

        guess = input('What is the VGS hotkey combination for this VGS voice line? ')

        while guess not in random_vgs_voice_line:
            guess = input(f'{Fore.RED}Wrong! Try again: {Style.RESET_ALL}')

        if guess in random_vgs_voice_line:
            print(f'{Fore.GREEN}Correct!{Style.RESET_ALL}\n')

            if argused == True:
                sys.exit()


def guess_talent(champions, argused, loop):
    random_champion = random.choice(champions)
    random_champion_talents_dir = files('paladle.talents').joinpath(random_champion)

    # This basically opens the directory and gets all the names of the files in there
    #talent_files = [f for f in os.listdir(random_champion_talents_dir) if os.path.isfile(os.path.join(random_champion_talents_dir, f))]

    # This selects a random file from the talent files
    #random_talent_file = random.choice(talent_files)

    # This opens the randomly selected file and reads the contents
    #file_path = os.path.join(random_champion_talents_dir, random_talent_file)
    #with open(file_path, 'r') as file:
    #    talent_desc = file.read()
    #    print(talent_desc)
    with as_file(random_champion_talents_dir) as dir_path:
        all_talent_files = [
            f for f in os.listdir(dir_path)
            if os.path.isfile(dir_path / f)
        ]
        random_talent_file = random.choice(all_talent_files)
        full_path = dir_path / random_talent_file

        with open(full_path, 'r') as file:
            talent_desc = file.read()
            print(talent_desc)

    guess = input('Which talent does this description belong to? ')
    while guess != random_talent_file:
        guess = input(f'{Fore.RED}Wrong! Try again: {Style.RESET_ALL}')

    if guess == random_talent_file:
        print(f'{Fore.GREEN}Correct!{Style.RESET_ALL}\n')

        if argused == True:
            sys.exit()

    if loop == True:
        #loopcheck = True
        main()

    elif loop == False:
        pass


if __name__ == '__main__':
    main()
