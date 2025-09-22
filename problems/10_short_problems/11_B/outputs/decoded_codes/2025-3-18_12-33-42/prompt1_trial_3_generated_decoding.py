# Start the program

# Receive user input:
targetNumber = abs(int(input()))  # Convert input to an integer and take the absolute value

# Initialize a counter variable:
index = 0

# Begin an infinite loop:
while True:
    # Calculate sumOfFirstN
    sumOfFirstN = index * (index + 1) / 2
    
    # Calculate difference
    difference = sumOfFirstN - targetNumber

    # Check conditions:
    if sumOfFirstN == targetNumber:
        print(index)
        break  # Exit the loop
    elif sumOfFirstN > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(index)
            break  # Exit the loop

    # Increment the counter:
    index += 1

# End of program
