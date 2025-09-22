# Step 1: Initialize Variables
n = abs(int(input()))  # Positive absolute value of user input
i = 0  # Initialize counter variable

# Step 2: Loop Until Condition is Met
while True:  # Repeat indefinitely
    # Calculate the triangular number s
    s = (i * (i + 1)) / 2  # s = (i * (i + 1)) / 2
    
    # Compute the difference m
    m = s - n  # m = s - n
    
    # Check Conditions
    if s == n:  # If s is equal to n
        print(i)  # Print the value of i (this is the answer)
        break  # End the loop
    elif s > n:  # Else if s is greater than n
        if m % 2 == 0:  # If m is an even number
            print(i)  # Print the value of i (this is also the answer)
            break  # End the loop
    
    # Increment the counter i by 1
    i += 1  # i = i + 1
