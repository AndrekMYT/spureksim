import random
import time

Gracz = input('Twoje imie')

hpp = 100
hps = 100
dmgs = random.randint(1,20)
dmgp = random.randint(1,20)
z1 = 1
z2 = 0

print('witamy w grze o Pani Spurek!!')


pktg = 1
print(' s - stay and heal, f - fight')
wybur = input('Co chcesz zrobic w pierwszej turze?')
if Gracz == 'Korwin' or Gracz == 'JKM':
    while hpp and hps > 0:
        if z1 >= z2 and wybur == 'f':
            print (f'Korwin atakuje')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            print(f' Tfu! geje mają jeszcze {hps} hp')
        elif z1 >= z2 and wybur == 's':
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            hpp = hpp + dmgs
            print('Cukier')
        elif z2 >= z1:
            print ('Tfu! geje atakują')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            print(f'Korwin ma jeszcze {hpp} hp')
            time.sleep(1)
            print(' s - stay and heal, f - fight')
            wybur = input('Co chcesz zrobic kucu?')           
        dmgs = random.randint(1,20)
        dmgp = random.randint(1,20)
        time.sleep(1)
    if hpp > hps:
        print(F'Korwin Wygrywa')
        print(f'Korwin ukonczył grę z {pktg} punktami. Kolejny lewak zmasakrowany!')
    else:
        print('Tfu!geje wygrywają ')
        print(f'Gdyby nie sen Korwin ukończyłby/a grę z {pktg} punktami')
elif Gracz == 'Admin' or Gracz == 'Administrator':
    while hpp and hps > 0:
        if z1 >= z2 and wybur == 'f':
            print (f'Admin atakuje')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            print(f'nony mają jeszcze {hps} hp')
        elif z1 >= z2 and wybur == 's':
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            hpp = hpp + dmgs
            print('BAN!')
        elif z2 >= z1:
            print ('nony  atakują')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            print(f'Admini mają jeszcze {hpp} hp')
            time.sleep(1)
            print(' s - stay and heal, f - fight')
            wybur = input('Co chcesz zrobic Adminie?')           
        dmgs = random.randint(1,20)
        dmgp = random.randint(1,20)
        time.sleep(1)
    if hpp > hps:
        print(F'Admini wygrywają!')
        print(f'Admini ukonczyli grę z {pktg} punktami. Kolejny non zbanowany!')
    else:
        print('nony wygrywają ')
        print(f'Gdyby nie tłum nonów Admini ukończyli grę z {pktg} punktami')
else:
    while hpp and hps > 0:
        if z1 >= z2 and wybur == 'f':
            print (f'{Gracz} atakuje')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            print(f' Spurek ma jeszcze {hps} hp')
        elif z1 >= z2 and wybur == 's':
            z1 = 0
            z2 = 1
            pktg = pktg + 1
            hpp = hpp + dmgs
            print('Kosiniak Kamysz mode on widze')
        elif z2 >= z1:
            print ('Spurek atakuje')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            print(f'{Gracz} ma jeszcze {hpp} hp')
            time.sleep(1)
            print(' s - stay and heal, f - fight')
            wybur = input('Co chcesz zrobic?')

        dmgs = random.randint(1,20)
        dmgp = random.randint(1,20)
        time.sleep(1)
    if hpp > hps:
        print(F'{Gracz} Wygrywa')
        print(f'{Gracz} ukonczył grę z {pktg} punktami. GG!')
    else:
        print('Spurek wygrywa')
        print(f'Gdyby nie smierć {Gracz} ukończyłby/a grę z {pktg} punktami')
    
