# Initialize Variables
n = abs(int(input()))  # takes the absolute value of user input
i = 0

# Start Infinite Loop
while True:
    # Calculate the Sum
    s = (i * (i + 1)) // 2  # using integer division for sum of first i natural numbers

    # Calculate the Difference
    m = s - n

    # Check for Match
    if s == n:
        print(i)
        break  # Exit the loop

    # Check for Exceeding Value
    if s > n:
        if m % 2 == 0:  # Check if m is divisible by 2
            print(i)
            break  # Exit the loop

    # Increment Loop Counter
    i += 1
