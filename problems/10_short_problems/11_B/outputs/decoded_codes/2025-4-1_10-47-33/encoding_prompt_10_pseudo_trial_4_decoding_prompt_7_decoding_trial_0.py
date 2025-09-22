# Initialize variable n as the absolute value of the integer input
n = abs(int(input()))

# Set variable i to 0
i = 0

# Infinite loop to find the result
while True:
    # Calculate the sum s as the sum of the first i integers
    s = i * (i + 1) // 2  # Using integer division for accuracy
    # Calculate the difference m as s - n
    m = s - n

    # If s is equal to n
    if s == n:
        # Print the value of i
        print(i)
        # Terminate the loop
        break

    # Else if s is greater than n
    elif s > n:
        # If m is even
        if m % 2 == 0:
            # Print the value of i
            print(i)
            # Terminate the loop
            break

    # Increment i by 1
    i += 1
