import random


def com_choose(*a):
    return  random.choice(a)

while True:
    com = com_choose('q','d','k')
    print(com)
    user =input('enter q(qayci), d(das), k(kagiz): ')
    if user not in ['q','d','k']:
        print('enter true key (q,d,k)')
    elif (com=='q'and user=='q') or (com=='d' and user=='d') or (com=='k' and user=='k'):
        print('it is tie gues again!')
    elif(com=='q'and user=='k') or (com=='d' and user=='q') or (com=='k' and user=='d'):
        print(f'computer guess: {com} and won game')
        break
    else:
        print(f'computer guess: {com} and user won game')
        break