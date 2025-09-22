# Get Input
targetNumber = int(input())  # Convert input to a non-negative integer

# Initialize Variables
currentInteger = 0

# Loop to Find the Result
while True:
    # Calculate the sum of all integers from 0 to currentInteger
    sumOfIntegers = sum(range(currentInteger + 1))
    # Calculate the difference
    difference = sumOfIntegers - targetNumber

    # Check Conditions
    if sumOfIntegers == targetNumber:
        print(currentInteger)  # Found the solution
        break
    elif sumOfIntegers > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentInteger)  # Found the solution
            break

    # Increase currentInteger to check the next integer
    currentInteger += 1
