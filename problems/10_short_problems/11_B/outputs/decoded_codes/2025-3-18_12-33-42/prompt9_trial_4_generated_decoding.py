# Start the program

# Receive Input
targetNumber = abs(int(input()))

# Initialize Variables
currentInteger = 0  # This will track the current integer being processed

# Begin Infinite Loop
while True:
    # Calculate Sum of Integers
    sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2  # Using integer division

    # Determine Difference
    difference = sumOfIntegers - targetNumber

    # Check for Equal Condition
    if sumOfIntegers == targetNumber:
        print(currentInteger)
        break  # Exit the loop

    # Check for Greater Condition
    if sumOfIntegers > targetNumber:
        if difference % 2 == 0:  # Check if difference is an even number
            print(currentInteger)
            break  # Exit the loop

    # Increment the Current Integer
    currentInteger += 1

# End program
