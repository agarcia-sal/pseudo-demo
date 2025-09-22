# BEGIN

# Assume n is an integer input from the user
n = abs(int(input()))  # Read input, convert to integer, and take absolute value

i = 0  # Initialize i to 0

while True:  # Loop indefinitely
    s = (i * (i + 1)) // 2  # Calculate the sum of first i integers
    m = s - n  # Calculate the difference between sum and n

    if s == n:  # Check if the sum equals n
        print(i)  # Output the value of i
        break  # Exit the loop

    elif s > n:  # Check if the sum exceeds n
        if m % 2 == 0:  # Check if the difference is even
            print(i)  # Output the value of i
            break  # Exit the loop

    i += 1  # Increment i by 1

# END
