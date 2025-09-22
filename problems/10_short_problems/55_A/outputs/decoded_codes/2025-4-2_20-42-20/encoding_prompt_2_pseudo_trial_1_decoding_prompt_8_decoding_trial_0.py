# Start the program.
numberOfElements = int(input())
isAvailable = [True] * numberOfElements
index = 0
increment = 1

while increment <= 500000:
    if isAvailable[index]:
        isAvailable[index] = False
    increment += 1
    index = (index + increment) % numberOfElements

remainingTrue = [elem for elem in isAvailable if elem]

if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')
