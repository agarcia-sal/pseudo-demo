# Start the program

# Step 2: Receive Input
targetValue = abs(int(input()))  # Read an integer and store its absolute value

# Step 3: Initialize Counter
index = 0  # Set index to 0

# Step 4: Infinite Loop
while True:
    # Step 4a: Calculate Triangle Number
    triangularNumber = (index * (index + 1)) // 2  # Use integer division

    # Step 4b: Calculate Difference
    difference = triangularNumber - targetValue

    # Step 4c: Check Conditions
    if triangularNumber == targetValue:
        print(index)  # Print index as result and exit
        break
    elif triangularNumber > targetValue:
        if difference % 2 == 0:
            print(index)  # Print index as result and exit
            break
    
    # Step 4d: Increment Counter
    index += 1  # Increase index by 1

# End of the program
