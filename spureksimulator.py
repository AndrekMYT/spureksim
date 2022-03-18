import random
import time

Gracz = input('Your name:')

hpp = 100
hps = 100
dmgs = random.randint(1,20)
dmgp = random.randint(1,20)
z1 = 1
z2 = 0

print('Welcome to the game about a Polish politician "Mrs. Spurek"!')
pktg = 1
print(' s - stay and heal, f - fight')
wybur = input('What do you want to do in your first turn?')
if Gracz == 'Korwin' or Gracz == 'JKM':
    dmgs = random.randint(1,20)
    dmgp = random.randint(1,20)
    while hpp > 0 and hps > 0:
        if z1 >= z2 and wybur == 'f':
            print (f'Korwin attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            if hps >0:
                print(f'Gays still have {hps} hp')
        elif z1 >= z2 and wybur == 's':
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            hpp = hpp + dmgs
            dmgs = random.randint(1,20)
            dmgp = random.randint(1,20)
            print('SUGAR')
        elif z2 >= z1:
            print ('Spurek atakuje')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            print(f'Korwin still has{hpp} hp')
            time.sleep(0.1)
            print(' s - stay and heal, f - fight')
            wybur = input('What do you want to do?')
        time.sleep(0.1)
    if hpp > hps:
        print(F'Korwin wins!')
        print(f'Korwin won the game with {pktg} points. GG!')
    else:
        print('Gays won :c')
        print(f'If not Korwin\'s death he would win the game with {pktg} points')
else:
    while hpp > 0 and hps > 0:
        dmgs = random.randint(1,20)
        dmgp = random.randint(1,20)
        if z1 >= z2 and wybur == 'f':
            print (f'{Gracz} attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            if hps > 0:
                print(f' Spurek still has {hps} hp')
        elif z1 >= z2 and wybur == 's':
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            hpp = hpp + dmgs
            dmgs = random.randint(1,20)
            dmgp = random.randint(1,20)
            print('Kosiniak Kamysz mode on I see')
        elif z2 >= z1:
            print ('Spurek attacks')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            if hpp > 0:
                print(f'{Gracz} still has {hpp} hp')
            time.sleep(0.1)
            print(' s - stay and heal, f - fight')
            wybur = input('What do you want to do?')
        time.sleep(0.1)
    if hpp > hps:
        print(f'{Gracz} wins the game with {pktg} points. GG!')
    else:
        print('Spurek wins')
        print(f'If not his death {Gracz} would win game with {pktg} points')
    
