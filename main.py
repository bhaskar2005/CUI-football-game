bhas = 0

while bhas <= 1000:
    print('\n')
    
    nu1 = ' THIS IS A FOOTBALL GAME '
    
    print(nu1.center(120, '*'))
    
    print('\n')
    
    nu2 = ' VERSION -- 1.6.3.7 '
    
    print(nu2.center(120, '_'))
    
    print('\n\n')


    
    name3 = str(input('Enter your competition name: '))
    
    print('\n\n')


    
    name1 = str(input('Enter Home team name: '))
    
    name2 = str(input('Enter away team name: '))
    
    print('\n\n')


    
    name11 = name1.title()
    
    name12 = name2.title()
    
    name13 = name3.upper()


    
    print('\n ' * 60)
    
    print('*' * 120)
    
    print('*' * 120)
    
    print('\n\n')
    
    print(name13.center(120))


    
    print('\nMatch between :	\t\t\t', name11, ' v/s ', name12)
    
    print('\n')


    
    j = 0
    
    a = 0
    
    c = 0
    
    print(name11, 'chances:\n')
    
    while a < 10:
    
        a = a + 1
    
        import random


    
        x = random.randrange(1, 7)


    
        num1 = int(input('Enter your number between 1 to 6: '))
    
        if num1 == x:
    
            c = c + 1
    
            print('next')
    
        else:
    
            print('next')


    
    e = 0
    
    f = 0
    
    print(name12, 'chances:\n')
    
    while e < 10:
    
        e = e + 1
    
        import random


    
        k = random.randrange(1, 7)


    
        num2 = int(input('Enter your number between 1 to 6: '))
    
        if num2 == k:
    
            f = f + 1
    
            print('next')
    
        else:
    
            print('next')


    
    # print('\n\n\t\t\t\t\t\tFinal RESULT -->  ', name11, ':', c, '-', f, ':', name12)
    
    if c > f:
    
        print('\n\t\t\t\t\t\t', name11, 'WINNER')
    
        print('\t\t\t\t\tCongratulation for wining!')
    
    elif c < f:
    
        print('\n\t\t\t\t', name12, 'WINNER')
    
        print('\t\t\tCongratulation for wining!')
    
    else:
    
        print('\n\t\t\t\tMatch is DRAW\n\n')


    
    print('\n ' * 60)
    
    print('*' * 120)
    
    print('*' * 120)


    
    print('\n')
    
    no1 = ' < REPORT CARD > '
    
    print(no1.center(120))


    
    import random


    
    x11 = random.randrange(40, 68)
    
    x12 = random.randrange(5, 19)
    
    x122 = random.randrange(5, 19)
    
    x13 = random.randrange(3, 10)
    
    x133 = random.randrange(3, 10)


    
    print('\n\t\t\t\t\t\t Scores : \t\t', name11, ':', c, ' - ', f, ':', name12)
    
    print('\t\t\t\t\t\t possession : \t', name11, ':', x11, '%', ' - ', 100 - x11, '%', ':', name12)
    
    print('\t\t\t\t\t\t Shorts : \t\t', name11, ':', x12, ' - ', x122, ':', name12)
    
    print('\t\t\t\t\t\t Corners : \t\t', name11, ':', x13, ' - ', x133, ':', name12)


    
    print('\n\n\n\n\nThanks for using,\t\t\t\t--- DEVELOPER : Bhaskar Roy\n\n')
    aaaa = str(input("Enter any key for next match: "))


    print('\n ' * 60)
