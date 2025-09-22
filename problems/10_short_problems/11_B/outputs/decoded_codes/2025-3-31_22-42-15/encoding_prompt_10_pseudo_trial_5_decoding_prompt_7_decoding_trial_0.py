# BEGIN

# Step 1: Initialize variables
n = 0  # To hold the user-specified positive integer
i = 0  # Counter to calculate the sum of natural numbers

# Step 2: Get user input
n = abs(int(input()))  # Read input and ensure it's a positive integer

# Step 3: Infinite loop to find the solution
while True:  # Loop until a break condition is met

    # Step 4: Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Use integer division to get the sum

    # Step 5: Calculate m as the difference between s and n
    m = s - n  # Calculate the difference

    # Step 6: Check if the sum is equal to the input n
    if s == n:  # If the calculated sum equals input n
        print(i)  # Output the result
        break  # Exit the loop

    # Step 7: Check if the sum exceeds the input n
    elif s > n:  # If the calculated sum surpasses input n
        # Step 8: Check if the difference m is even
        if m % 2 == 0:  # If the difference is even
            print(i)  # Output the result
            break  # Exit the loop

    # Step 9: Increment i for the next iteration
    i += 1  # Move to the next natural number

# END
