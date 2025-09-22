# 1. Receive and Prepare Input
targetNumber = int(input())

# 2. Initialize Variables
currentIndex = 0

# 3. Process to Find the Desired Index
while True:
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2
    difference = triangularNumber - targetNumber
    
    if triangularNumber == targetNumber:
        print(currentIndex)
        break
    elif triangularNumber > targetNumber:
        if difference % 2 == 0:
            print(currentIndex)
            break
    
    currentIndex += 1
