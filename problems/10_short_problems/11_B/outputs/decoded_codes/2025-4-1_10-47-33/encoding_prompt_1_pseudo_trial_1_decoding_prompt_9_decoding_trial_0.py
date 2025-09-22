# Start the program
# Get the absolute value of user input as an integer
n = abs(int(input()))  # Read user input and convert it to an absolute integer

# Initialize i to 0
i = 0

# Enter an infinite loop
while True:
    # Calculate the sum s of the first i natural numbers
    s = i * (i + 1) // 2  # Using integer division for sum calculation

    # Calculate the difference m between s and n
    m = s - n  # This represents how far s is from n

    # Check if s is equal to n
    if s == n:
        print(i)  # Print the value of i
        break  # Exit the loop

    # Check if s is greater than n
    if s > n:
        # Check if m is even
        if m % 2 == 0:
            print(i)  # Print the value of i
            break  # Exit the loop

    # Increment i by 1
    i += 1
