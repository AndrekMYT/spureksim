import random
import time

Gamer = input('Your name:')

hpp = 100
hps = 100
dmgs = random.randint(1,20)
dmgp = random.randint(1,20)
z1 = 1
z2 = 0

print('Welcome to the game about a Polish politician "Mrs. Spurek"!')
pktg = 1
print('h - heal (-1 point), f - fight')
choice = input('What do you want to do in your first turn? ')
if Gamer == 'Korwin' or Gamer == 'JKM':
    dmgs = random.randint(1,20)
    dmgp = random.randint(1,20)
    while hpp > 0 and hps > 0:
        if z1 >= z2 and choice == 'f':
            print ('Korwin attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps >0:
                print(f'Gays still have {hps} hp')
        elif z1 >= z2 and choice == 'h':
            if pktg > 0:
                z1 = 0
                z2 = 1
                pktg -=1
                hpp = hpp + dmgs
                dmgs = random.randint(1,20)
                dmgp = random.randint(1,20)
                print('SUGAR')
            z1 = 0
            z2 = 1
        elif z1 >= z2 and choice != 'f' and choice != 'h':
            print ('Korwin attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps >0:
                print(f'Gays still have {hps} hp')
        elif z2 >= z1:
            print ('Korwin attacks')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            print(f'Korwin still has {hpp} hp')
            time.sleep(0.1)
            print(' h - heal (-1 point), f - fight')
            print(f'You have {pktg} points')
            choice = input('What do you want to do? ')
        time.sleep(0.1)
    if hpp > hps:
        print(F'Korwin wins!')
        print(f'Korwin won the game with {pktg} points. GG!')
    else:
        print('Gays won :c')
        print(f'If not Korwin\'s death he would win the game with {pktg} points')
elif Gamer == 'joe mama' or Gamer == 'ur mom' or Gamer == 'Joe mama':
    dmgs = random.randint(1,20)
    dmgp = random.randint(1,20)
    while hpp > 0 and hps > 0:
        if z1 >= z2 and choice == 'f':
            print ('Joe mama attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps >0:
                print(f'Joe dada still have {hps} hp')

        elif z1 >= z2 and choice == 'h':
            if pktg > 0:
                z1 = 0
                z2 = 1
                pktg -=1
                hpp = hpp + dmgs
                dmgs = random.randint(1,20)
                dmgp = random.randint(1,20)
                print('Joe mama got new pan')
            z1 = 0
            z2 = 1
        elif z1 >= z2 and choice != 'f' and choice != 'h':
            print ('Joe mama attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps >0:
                print(f'Joe dada still have {hps} hp')
        elif z2 >= z1:
            print ('Joe dada attacks')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            if hpp > 0:
                print(f'Joe mama still has {hpp} hp')
            time.sleep(0.1)
            print('  h - heal (-1 point), f - fight')
            print(f'You have {pktg} points')
            choice = input('What do you want to do? ')
        time.sleep(0.1)
    if hpp > hps:
        print(F'Joe mama wins!')
        print(f'Joe mama  won the game with {pktg} points. GG!')
    else:
        print('Joe dada won')
        print(f'If not Imposter\'s death he would win the game with {pktg} points')
elif Gamer == 'amogus' or Gamer == 'Impostor' or Gamer == 'Imposter':
    dmgs = random.randint(1,20)
    dmgp = random.randint(1,20)
    while hpp > 0 and hps > 0:
        if z1 >= z2 and choice == 'f':
            print ('Impostor attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps >0:
                print(f'Crewmates still have {hps} hp')

        elif z1 >= z2 and choice == 'h':
            if pktg > 0:
                z1 = 0
                z2 = 1
                pktg -=1
                hpp = hpp + dmgs
                dmgs = random.randint(1,20)
                dmgp = random.randint(1,20)
                print('Crewmate Killed')
            z1 = 0
            z2 = 1
        elif z1 >= z2 and choice != 'f' and choice != 'h':
            print ('Impostor attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps >0:
                print(f'Crewmates still have {hps} hp')
        elif z2 >= z1:
            print ('Crewmates attack')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            if hpp > 0:
                print(f'Impostor still has {hpp} hp')
            time.sleep(0.1)
            print('  h - heal (-1 point), f - fight')
            print(f'You have {pktg} points')
            choice = input('What do you want to do? ')
        time.sleep(0.1)
    if hpp > hps:
        print(F'Impostor wins!')
        print(f'Impostor won the game with {pktg} points. GG!')
    else:
        print('Crewmates won SUS')
        print(f'If not Imposter\'s death he would win the game with {pktg} points')
else:
    while hpp > 0 and hps > 0:
        dmgs = random.randint(1,20)
        dmgp = random.randint(1,20)
        if z1 >= z2 and choice == 'f':
            print (f'{Gamer} attacks')
            hps = hps - dmgp
            z1 = 0
            z2 = 1
            pktg +=1
            if hps > 0:
                print(f' Spurek still has {hps} hp')
        elif z1 >= z2 and choice == 'h':
            if pktg > 0:
                z1 = 0
                z2 = 1
                pktg -=1
                hpp = hpp + dmgs
                dmgs = random.randint(1,20)
                dmgp = random.randint(1,20)
                print('Kosiniak Kamysz mode on I see')
            z1 = 0
            z2 = 1
        elif z2 >= z1:
            print (f'{Gamer} attacks')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            print(f'Spurek still has {hps} hp')
            time.sleep(0.1)
            print(' h - heal (-1 point), f - fight')
            print(f'You have {pktg} points')
            choice = input('What do you want to do? ')
        elif z2 >= z1:
            print ('Spurek attacks')
            hpp = hpp - dmgs
            z1 = 1
            z2 = 0
            if hpp > 0:
                print(f'{Gamer} still has {hpp} hp')
            time.sleep(0.1)
            print(' h - heal (-1 point), f - fight')
            print(f'You have {pktg} points')
            choice = input('What do you want to do? ')
        time.sleep(0.1)
    if hpp > hps:
        print(f'{Gamer} wins the game with {pktg} points. GG!')
    else:
        print('Spurek wins')
        print(f'If not his death {Gamer} would win game with {pktg} points')
    
