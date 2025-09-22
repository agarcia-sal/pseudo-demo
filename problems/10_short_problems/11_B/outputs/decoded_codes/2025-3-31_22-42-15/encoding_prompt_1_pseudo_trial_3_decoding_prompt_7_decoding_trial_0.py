# Start of the program

# Step 2: Receive Input
# Read an integer from user input and store its absolute value in targetValue
targetValue = abs(int(input()))

# Step 3: Initialize Counter
# Set the initial value of index
index = 0

# Step 4: Infinite Loop
while True:
    # Step 4a: Calculate Triangle Number
    # Compute the triangular number using the formula
    triangularNumber = (index * (index + 1)) // 2
    
    # Step 4b: Calculate Difference
    # Determine the difference from the target value
    difference = triangularNumber - targetValue
    
    # Step 4c: Check Conditions
    # If triangularNumber equals targetValue, print index and exit
    if triangularNumber == targetValue:
        print(index)
        break
    
    # Else if triangularNumber is greater than targetValue
    elif triangularNumber > targetValue:
        # If the difference is even, print index and exit
        if difference % 2 == 0:
            print(index)
            break
    
    # Step 4d: Increment Counter
    # Increase the index for the next iteration
    index += 1

# End of the program
