# Start
targetNumber = abs(int(input()))
currentIndex = 0

while True:
    # Calculate the sum of the first currentIndex natural numbers
    currentSum = currentIndex * (currentIndex + 1) // 2  # Using the formula n(n+1)/2
    difference = currentSum - targetNumber
    
    if currentSum == targetNumber:
        print(currentIndex)
        break
    elif currentSum > targetNumber:
        if difference % 2 == 0:
            print(currentIndex)
            break
            
    currentIndex += 1
# End


# Example of improved input handling
try:
    targetNumber = abs(int(input()))
except ValueError:
    print("Please enter a valid integer.")
    exit(1)
