# Start of the program

# Declare integer variable n and initialize it with the absolute value of input
n = abs(int(input()))

# Declare integer variable i and initialize it to 0
i = 0

# Begin while loop to find the required conditions
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Using integer division for precise results
    
    # Calculate the difference between s and n
    m = s - n

    # Check if the sum equals n
    if s == n:
        print(i)  # Output the value of i if the sum equals n
        break  # Exit the loop

    # Check if the sum is greater than n
    elif s > n:
        if m % 2 == 0:  # Check if the difference is even
            print(i)  # Output the value of i if m is even
            break  # Exit the loop

    # Increment i to move to the next integer
    i += 1

# End of the program
