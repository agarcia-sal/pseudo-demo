# 1. Initialize Variables
n = abs(int(input()))  # Set n to the absolute value of the integer received as input
i = 0  # Set i to 0, which will be used to track the current integer candidate

# 2. Loop Indefinitely
while True:  # Repeat the following steps until a suitable integer is found
    # a. Calculate Sum
    s = (i * (i + 1)) // 2  # Compute the sum s of the first i integers

    # b. Determine Difference
    m = s - n  # Calculate m as the difference between s and n

    # c. Check for Conditions
    if s == n:  # If the computed sum s equals n
        print(i)  # Print the value of i (the current integer) and exit the loop
        break  # Exit the loop
    
    if s > n:  # If the computed sum s is greater than n
        if m % 2 == 0:  # Check if the difference m is even
            print(i)  # Print the value of i and exit the loop
            break  # Exit the loop

    # d. Increment Counter
    i += 1  # Increase the value of i by 1 to check the next integer
