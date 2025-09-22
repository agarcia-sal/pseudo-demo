# Start of the program

# Read an integer input and take its absolute value
n = abs(int(input()))

# Initialize the counter variable i to 0
i = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Using integer division

    # Calculate the difference between the sum and n
    m = s - n
    
    # Check if the sum exactly equals n
    if s == n:
        print(i)  # Output i if the sum equals n
        break  # Exit the loop

    # Check if the sum is greater than n
    elif s > n:
        # Check if the difference m is even
        if m % 2 == 0:
            print(i)  # Output i if m is even
            break  # Exit the loop

    # Increment i to examine the next integer
    i += 1

# End of the program
