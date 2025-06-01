#!/usr/bin/env python3

import random
from playsound import playsound
import requests
import tempfile

def main():
    champions = ['androxus', 'maeve', 'ying']
    
    guess_the_ult_voiceline_text(champions)
    guess_the_voiceline_sound(champions)
    guess_the_ability(champions)
    guess_vgs_keys()
    guess_talent(champions)

def guess_the_ult_voiceline_text(champions):
    random_champion = random.choice(champions)
    champ_file = open(f'voicelines_text/{random_champion}', 'r')
    content = champ_file.read()
    print(content)
    champ_file.close()

    guess = input('Which champions ult voices lines are these? ')
    wrong_guess = [0, 1, 2, 3, 4]
    hint = random_champion[0]

    while guess != random_champion:
        for i in wrong_guess:
            print('Wrong!')
            if i == 4:
                print(f'Hint: The champions name starts with {hint}')
            guess = input('Try again: ')

    if guess == random_champion:
        print('Correct!\n')

def guess_the_ability(champions):
    random_champion = random.choice(champions)
    champ_file = open(f'ability_names/{random_champion}', 'r')
    content = champ_file.read().splitlines()
    random_line = random.choice(content)
    print(random_line)
    champ_file.close()

    guess = input('Which champion is this ability/weapon name from? ')
    hint = random_champion[0]

    while guess != random_champion:
        for i in range(0,3):
            print('Wrong!')
            if i == 4:
                print(f'Hint: The champions name starts with {hint}')
            guess = input('Try again: ')

    if guess == random_champion:
        print('Correct!\n')

def guess_the_voiceline_sound(champions):
    voice_files = ['_TR_FirstBlood', '_VGS_Other_G_M']
    random_voice_file = random.choice(voice_files)
    random_champion = random.choice(champions)
    playsound(f'voicelines_audio/{random_champion}{random_voice_file}.ogg')

    guess = input('Which champion is this voice line from? ')
    wrong_guess = [0, 1, 2, 3, 4]
    hint = random_champion[0]

    while guess != random_champion:
        for i in wrong_guess:
            print('Wrong!')
            if i == 4:
                print(f'Hint: The champions name starts with {hint}')
                playsound(f'voicelines_audio/{random_champion}{random_voice_file}.ogg')
            guess = input('Try again: ')

    if guess == random_champion:
        print('Correct!\n')

def guess_vgs_keys():
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

        if guess not in random_vgs_voice_line:
            while guess not in random_vgs_voice_line:
                guess = input('Wrong! Try again: ')

        if guess in random_vgs_voice_line:
            print('Correct!\n')


def guess_talent(champions):
    random_champion = random.choice(champions)
    champ_file = open(f'talents/{random_champion}', 'r')
    content = champ_file.read()
    print(content)
    champ_file.close()



if __name__ == '__main__':
    main()
