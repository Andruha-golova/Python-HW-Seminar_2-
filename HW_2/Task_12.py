S = int(input('inter number S: '))
P = int(input('inter number P: '))
for x in range(1, S):
    for y in range(1, P):
        if y + x == S and x * y == P:
            print(f'First hidden number {x}, second hidden number {y}')
            break
    else:
        continue
    break