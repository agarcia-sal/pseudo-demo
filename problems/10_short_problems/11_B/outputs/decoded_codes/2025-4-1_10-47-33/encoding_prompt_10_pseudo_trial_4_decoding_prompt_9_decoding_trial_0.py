# Initialize variable n as the absolute value of the integer input
n = abs(int(input()))

# Set variable i to 0
i = 0

# Loop indefinitely until a condition is met to break out
while True:
    # Calculate the sum s as the sum of the first i integers
    s = i * (i + 1) // 2  # Using integer division
    
    # Calculate the difference m as s - n
    m = s - n

    # Check if s is equal to n
    if s == n:
        print(i)  # Print the value of i
        break  # Terminate the loop

    # Check if s is greater than n
    elif s > n:
        # Check if m is even
        if m % 2 == 0:
            print(i)  # Print the value of i
            break  # Terminate the loop

    # Increment i by 1
    i += 1
