def win_option(user, comp):
    options = ['rock', 'gun', 'lightning', 'devil', 'dragon',
          'water', 'air', 'paper', 'sponge', 'wolf', 'tree',
          'human', 'snake', 'scissors', 'fire']
    sets = set()
    i = options.index(user) - 1
    for _ in range(7):
        sets.add(options[i])
        i -= 1
    if comp in sets:
        return True
    else:
        return False
def list_rating(rates):
    dicts = {}
    with open(rates, 'r') as f:
        for i in f:
            key, values = i.split(' ')
            dicts[key] = int(values)
    return dicts
import random
name = input('Enter your name: ')
print(f'Hello, {name}')
options = input().split(',')
if len(options) == 1:
    options = ['rock', 'paper', 'scissors']
print('Okay, let\'s start')
spi = list_rating('rating.txt')
if name not in spi:
    spi[name] = 0
while True:
    user = input()
    comp = random.choice(options)
    if '!exit' == user:
        print('Bye!')
        break
    elif '!rating' == user:
        print(f'Your rating: {spi[name]}')
    elif user not in options:
        print('Invalid input')
    elif user == comp:
        spi[name] += 50
        print(f'There is a draw ({user})')
    elif win_option(user, comp):
        spi[name] += 100
        print(f'Well done. The computer chose {comp} and failed')
    else:
        print(f'Sorry, but the computer chose {comp}')


