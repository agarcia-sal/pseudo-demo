# Start
# Read absolute input value
n = int(input())  # Input: non-negative integer

# Initialize a counter variable
i = 0  # Set i to 0

# Loop indefinitely
while True:
    # Calculate the sum of first i integers
    s = (i * (i + 1)) / 2  # Use the formula to calculate the sum

    # Calculate the difference
    m = s - n  # Set m to the difference between s and n

    # Check the value of s against n
    if s == n:
        print(i)  # Output i
        break  # Terminate the loop
    elif s > n:
        if m % 2 == 0:  # Check if m is an even number
            print(i)  # Output i
            break  # Terminate the loop

    # Increment the counter
    i += 1  # Increase i by 1
# End
