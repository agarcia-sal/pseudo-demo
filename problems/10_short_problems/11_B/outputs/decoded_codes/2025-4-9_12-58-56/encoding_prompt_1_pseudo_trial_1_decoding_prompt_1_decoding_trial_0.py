# 1. Start the Program

# 2. Get Input
targetNumber = abs(int(input()))

# 3. Initialize Variables
currentIndex = 0  # currentIndex is initialized to 0

# 4. Continuous Loop
while True:  # repeat indefinitely
    
    # a. Calculate Sum
    sumOfFirstCurrent = (currentIndex * (currentIndex + 1)) / 2
    
    # b. Determine Difference
    difference = sumOfFirstCurrent - targetNumber
    
    # c. Check Conditions
    # Condition 1
    if sumOfFirstCurrent == targetNumber:
        print(currentIndex)
        break  # Exit the loop
    
    # Condition 2
    if sumOfFirstCurrent > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)
            break  # Exit the loop
    
    # d. Increment Current Index
    currentIndex += 1  # Increase currentIndex by 1

# 5. End of Program
