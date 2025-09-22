# Step 1: Read input and initialize
n = int(abs(input()))  # Get absolute value of user input and convert to integer
i = 0  # Initialize counter

# Step 3: Start an infinite loop
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Use integer division
    # Compute the difference m
    m = s - n

    # If s equals n
    if s == n:
        print(i)  # Print i
        break  # Exit the loop
    # Else if s is greater than n
    elif s > n:
        # If m is an even number
        if m % 2 == 0:
            print(i)  # Print i
            break  # Exit the loop
    # Increment i by 1
    i += 1  # Check the next integer
