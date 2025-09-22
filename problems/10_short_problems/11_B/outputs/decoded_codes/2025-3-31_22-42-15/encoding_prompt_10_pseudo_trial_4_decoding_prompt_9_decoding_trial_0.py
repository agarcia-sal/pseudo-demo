# Initialize variable n to the absolute value of the user input
n = abs(int(input()))
# Initialize loop counter i
i = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Using floor division to ensure integer result

    # Calculate the difference
    m = s - n

    # Check if the sum equals the absolute input
    if s == n:
        print(i)
        break  # Exit the loop

    # Check if the sum exceeds the absolute input
    if s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)
            break  # Exit the loop

    # Increment the loop counter
    i += 1
