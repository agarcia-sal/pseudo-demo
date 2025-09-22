# Input
targetNumber = abs(int(input()))

# Initialize
currentIndex = 0

# Loop
while True:
    # Calculate the sum of the first currentIndex integers
    sumOfFirstN = (currentIndex * (currentIndex + 1)) / 2
    
    # Calculate the difference
    difference = sumOfFirstN - targetNumber
    
    # Check Conditions
    if sumOfFirstN == targetNumber:
        print(currentIndex)  # Desired result
        break
    
    elif sumOfFirstN > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)  # Desired result
            break
    
    # Increment currentIndex
    currentIndex += 1
