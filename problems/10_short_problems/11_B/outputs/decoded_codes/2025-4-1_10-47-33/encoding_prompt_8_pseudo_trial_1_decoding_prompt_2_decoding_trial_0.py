# Get Input
targetNumber = int(input())  # Convert input to a non-negative integer

# Initialize Variables
currentInteger = 0

# Loop to Find the Result
while True:
    # Calculate the sum of all integers from 0 to currentInteger
    sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2
    
    # Calculate the difference
    difference = sumOfIntegers - targetNumber
    
    # Check Conditions
    if sumOfIntegers == targetNumber:
        print(currentInteger)  # The solution
        break
    elif sumOfIntegers > targetNumber:
        # Check if difference is even
        if difference % 2 == 0:
            print(currentInteger)  # The solution
            break
    
    # Increase currentInteger by 1
    currentInteger += 1
