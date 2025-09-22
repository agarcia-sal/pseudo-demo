# Start of the program

# Step 2: Input - reading a number from the user and taking its absolute value
n = abs(int(input()))  # Get user input, convert to integer, and take absolute value

# Step 3: Initialize variable 'i' to 0
i = 0

# Step 4: Loop indefinitely until the break condition is met
while True:
    # Step 4.1: Calculate 's' using the formula for the sum of the first i integers
    s = (i * (i + 1)) / 2
    
    # Step 4.2: Compute 'm' as the difference between s and n
    m = s - n
    
    # Step 4.3: Check conditions
    # If s is equal to n
    if s == n:
        print(i)  # Output the current value of 'i'
        break  # Exit the loop
    
    # Else if s is greater than n
    elif s > n:
        # If m is even
        if m % 2 == 0:
            print(i)  # Output the current value of 'i'
            break  # Exit the loop
    
    # Step 4.4: Increment 'i' by 1 for the next iteration
    i += 1

# End of the program
