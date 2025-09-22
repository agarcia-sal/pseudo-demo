# 1. Initialize Variables
n = abs(int(input()))  # Getting user input and converting to absolute integer
i = 0  # Counter for current integer candidate

# 2. Loop Indefinitely
while True:
    # a. Calculate Sum
    s = (i * (i + 1)) / 2  # Sum of first i integers

    # b. Determine Difference
    m = s - n  # Difference between sum and n

    # c. Check for Conditions
    if s == n:  # If the computed sum equals n
        print(i)  # Print the value of i
        break  # Exit the loop
        
    if s > n:  # If the computed sum is greater than n
        if m % 2 == 0:  # Check if the difference m is even
            print(i)  # Print the value of i
            break  # Exit the loop
            
    # d. Increment Counter
    i += 1  # Increase the value of i to check the next integer

# 3. End of Algorithm
