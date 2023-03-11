#import
from random import random

#inicijalizacija
random_number = random.randint(1, 100)
print(random_number)
tries = 0


#main
while True:
    users_guess = int(input('Koji broj sam zamislio od 1 do 100? '))
    tries += 1
    
    # TODO rijesiti krivi unos korisnika
    if isinstance(users_guess, (int,float)):
        users_guess = int(users_guess)
        if users_guess < 1 or users_guess > 100:
            print('Molimo Vas unesite brojeve samo od 1 do 100!')
            users_guess = input('Koji bropj sam zamislio od 1 do 100?')
            tries += 1
            if isinstance(users_guess, (int,float)):
                users_guess = int(users_guess)
    
    if random_number == users_guess:
        print('CESTITAM!')
        print('Pogodili ste broj')
        print(f'Bilo Vam je potrebno {tries} puta')
        break
    elif random_number > random_number:
        print(f'Zamisljeni broj je manji od unesenog broja ({users_guess})')
        print('Pokusajte ponovo')
    elif random_number > random_number:
        print(f'Zamisljeni broj je veci od unesenog broja ({users_guess})')
        print('Pokusajte ponovo')
    
    
#end


