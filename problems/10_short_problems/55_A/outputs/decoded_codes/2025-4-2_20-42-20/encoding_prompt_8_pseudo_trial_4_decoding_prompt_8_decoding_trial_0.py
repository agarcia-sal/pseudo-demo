n = int(input())
positions = [True] * n
currentIndex = 0
step = 1

while step <= 500000:
    if positions[currentIndex]:
        positions[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % n

unmarkedPositions = [pos for pos in positions if pos]

if len(unmarkedPositions) == 0:
    print('YES')
else:
    print('NO')


def can_mark_all(n):
    positions = [True] * n
    currentIndex = 0
    step = 1

    while step <= 500000:
        if positions[currentIndex]:
            positions[currentIndex] = False
        step += 1
        currentIndex = (currentIndex + step) % n

    return len([pos for pos in positions if pos]) == 0

n = int(input())
if can_mark_all(n):
    print('YES')
else:
    print('NO')
