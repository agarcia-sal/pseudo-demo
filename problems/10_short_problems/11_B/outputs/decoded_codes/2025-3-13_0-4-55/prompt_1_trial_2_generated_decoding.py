# Step 1: Initialize Variables
n = abs(int(input()))  # Get the absolute value of the integer input
i = 0  # Counter for the current integer candidate

# Step 2: Loop Indefinitely
while True:
    
    # a. Calculate Sum
    s = (i * (i + 1)) // 2  # Compute the sum of the first i integers (using integer division)

    # b. Determine Difference
    m = s - n  # Calculate the difference between sum s and n

    # c. Check for Conditions
    if s == n:  # If the computed sum s equals n
        print(i)  # Print the current integer i
        break  # Exit the loop

    if s > n:  # If the computed sum s is greater than n
        if m % 2 == 0:  # Check if the difference m is even
            print(i)  # Print the current integer i
            break  # Exit the loop
    
    # d. Increment Counter
    i += 1  # Increase the value of i by 1
