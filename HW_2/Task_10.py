import random
n = int(input('Enter the number of coins: '))
avers = revers = 0
for _ in range(n):
    a = (random.randint(0, 1))
    print(a, end = ' ')
    if a == 0: avers += 1
    else: revers += 1
if avers > revers:
    print(f'\nMinimum number of coins to flip {revers}')
else: print(f'\nMinimum number of coins to flip {avers}')