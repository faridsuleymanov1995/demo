import random


list1 = ['''
     _______
----'   ____)____
           ________)
           _________)
          _________)
----.____________)''', '''     
     _______
----'   ____)______
           ________)
           _________)
          (_____)
----._____(____)''','''
     _______
----'   ____)
          (______)
          (______)
          (_____)
----._____(____)''']


a = 'kqd'
while True:

    com = (lambda x : random.choice(x))([list1[0],list1[1],list1[2]])
    user =input('enter q(qayci), d(das), k(kagiz): ')
    if user not in ['q','d','k']:
        print('enter true key (q,d,k)')
    elif (com==list1[1] and user=='q') or (com==list1[2] and user=='d') or (com==list1[0] and user=='k'):
        print('it is tie gues again!')
    elif(com==list1[1] and user=='k') or (com==list1[2] and user=='q') or (com==list1[0] and user=='d'):
        print(f'computer guess: {com}  \nyour is {list1[a.index(user)]}  \n computer  won game')
        break
    else:
        print(f'computer guess: {com}  \nyour is {list1[a.index(user)]}  \n user won game')
        break