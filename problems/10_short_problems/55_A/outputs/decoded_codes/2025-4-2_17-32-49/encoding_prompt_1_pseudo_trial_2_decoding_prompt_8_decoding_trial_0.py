# Input
n = int(input())

# Initialization
isPresent = [True] * n
index = 0
step = 1

# Processing Loop
while step <= 500000:
    if isPresent[index]:
        isPresent[index] = False
    step += 1
    index = (index + step) % n

# Checking Results
availablePositions = [pos for pos in isPresent if pos]
if len(availablePositions) == 0:
    print("YES")
else:
    print("NO")
