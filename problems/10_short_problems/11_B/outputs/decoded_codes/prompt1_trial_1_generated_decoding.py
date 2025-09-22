# Step 1: Initialize Variables
n = abs(int(input()))  # Set n to the absolute value of the integer received as input
i = 0  # Set i to 0, the integer candidate

# Step 2: Loop Indefinitely
while True:
    # Step 2a: Calculate Sum
    s = (i * (i + 1)) // 2  # Compute the sum s of the first i integers

    # Step 2b: Determine Difference
    m = s - n  # Calculate m as the difference between s and n

    # Step 2c: Check for Conditions
    if s == n:  # Check if the computed sum s equals n
        print(i)  # Print the value of i
        break  # Exit the loop

    if s > n:  # Check if the computed sum s is greater than n
        if m % 2 == 0:  # Check if the difference m is even
            print(i)  # Print the value of i
            break  # Exit the loop

    # Step 2d: Increment Counter
    i += 1  # Increase the value of i by 1 to check the next integer
