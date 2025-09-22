# Get Input
targetNumber = int(input())  # Convert input to a non-negative integer

# Initialize Variables
currentInteger = 0

# Loop to Find the Result
while True:  # Start an endless loop
    # Calculate the sum of all integers from 0 to currentInteger
    sumOfIntegers = sum(range(currentInteger + 1))  # Using sum function to directly compute the sum

    # Calculate the difference
    difference = sumOfIntegers - targetNumber

    # Check Conditions
    if sumOfIntegers == targetNumber:
        print(currentInteger)  # Print the solution
        break  # Exit the loop
    elif sumOfIntegers > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentInteger)  # Print the solution
            break  # Exit the loop

    # Increase currentInteger for the next iteration
    currentInteger += 1
