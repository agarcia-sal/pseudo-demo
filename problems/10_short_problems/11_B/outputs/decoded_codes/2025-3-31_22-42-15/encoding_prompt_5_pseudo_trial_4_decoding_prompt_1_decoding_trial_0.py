# 1. Start the program

# 2. Get user input
targetValue = abs(int(input()))

# 3. Initialize a counter
counter = 0

# 4. Begin an endless loop to find the triangular number
while True:
    # a. Calculate the triangular number
    triangularNumber = (counter * (counter + 1)) // 2
    
    # b. Calculate the difference
    difference = triangularNumber - targetValue
    
    # c. If triangularNumber is equal to targetValue
    if triangularNumber == targetValue:
        print(counter)  # Found a match
        break  # Exit the loop

    # d. Else if triangularNumber is greater than targetValue
    elif triangularNumber > targetValue:
        # If difference is an even number
        if difference % 2 == 0:
            print(counter)  # Different condition met
            break  # Exit the loop
    
    # e. Increment counter by 1
    counter += 1

# 5. End the program
