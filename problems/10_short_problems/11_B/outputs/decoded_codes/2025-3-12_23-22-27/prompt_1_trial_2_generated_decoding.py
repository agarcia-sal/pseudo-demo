# 1. Initialize Variables
n = abs(int(input()))  # Get the absolute value of the integer received as input
i = 0  # Initialize counter

# 2. Loop Indefinitely
while True:
    # a. Calculate Sum
    s = (i * (i + 1)) / 2  # Compute the sum of the first i integers
    
    # b. Determine Difference
    m = s - n  # Calculate the difference between s and n
    
    # c. Check for Conditions
    if s == n:
        print(i)  # Print the value of i and exit loop
        break  # Exit the loop
    elif s > n:
        if m % 2 == 0:  # Check if the difference m is even
            print(i)  # Print the value of i and exit loop
            break  # Exit the loop
    
    # d. Increment Counter
    i += 1  # Increase the value of i by 1 to check the next integer
