# 1. Initialize Variables:
n = abs(int(input()))  # Get the absolute value of the integer input.
i = 0  # This will be the current integer candidate.

# 2. Loop Indefinitely:
while True:
    # a. Calculate Sum:
    s = (i * (i + 1)) // 2  # Compute the sum of the first i integers.

    # b. Determine Difference:
    m = s - n  # Calculate the difference between s and n.

    # c. Check for Conditions:
    if s == n:  # Check if the computed sum equals n.
        print(i)  # Print the value of i and exit the loop.
        break  # Exit the loop.
    
    if s > n:  # If the computed sum is greater than n:
        if m % 2 == 0:  # Check if the difference m is even:
            print(i)  # Print the value of i and exit the loop.
            break  # Exit the loop.

    # d. Increment Counter:
    i += 1  # Increase the value of i by 1 to check the next integer.
