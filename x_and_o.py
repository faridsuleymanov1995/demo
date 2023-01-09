def show():
    a = []
    x = 3

    for i in range(3):
        for j in range(-2+x,1+x):
            a.append(j)
        print(tuple(a))
        a.clear()
        x+=3
print('you have to play by choosing number put x or o : ')
print('in order to exit game simply type "end" ')
show()
x = [' 'for i in range(1,10)]
gorsel =[]

while True:

    def player1():
        player1 = input('enter number player1: ')
        if player1 ==  'end':
            return 'end'
        b = 0
        for i in range(1,10):
            if i==int(player1):
                x.pop(i-1)
                x.insert(i-1 , 'x')
        for j in x:
            gorsel.append(j)
            if b==2:
                print(gorsel)
                gorsel.clear()
                b=-1

            b+=1

    if player1()== 'end' :
        break
    def player2():
        player2 = input('enter number player2: ')
        b = 0
        if player2=='end':
            return 'end'
        for i in range(1,10):
            if i==player2:
                x.pop(i-1)
                x.insert(i-1 , 'o')
        for j in x:
            gorsel.append(j)
            if b==2:
                print(gorsel)
                gorsel.clear()
                b=-1

            b+=1




    if player2()=='end':
        break
