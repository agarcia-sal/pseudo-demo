# Initialize Variables
n = abs(int(input()))  # Set variable n to the absolute value of the input
i = 0  # Initialize loop counter

# Start Infinite Loop
while True:
    # Calculate the Sum
    s = (i * (i + 1)) // 2  # Calculate the sum of the first i natural numbers

    # Calculate the Difference
    m = s - n  # Calculate the difference between s and n

    # Check for Match
    if s == n:
        print(i)  # Print the value of i
        break  # Exit the loop

    # Check for Exceeding Value
    if s > n:
        if m % 2 == 0:  # Check if m is divisible by 2
            print(i)  # Print the value of i
            break  # Exit the loop

    # Increment Loop Counter
    i += 1  # Increase i by 1
