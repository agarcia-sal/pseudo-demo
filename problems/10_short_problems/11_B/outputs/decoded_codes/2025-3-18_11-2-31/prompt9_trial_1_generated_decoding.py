# Initialize necessary variables
n = abs(int(input()))  # Get the absolute value of the integer input from the user
i = 0  # Initialize the counter to zero

# Begin an infinite loop to calculate and check sums
while True:
    # Calculate the sum of the first i integers
    s = (i * (i + 1)) // 2  # Use integer division to get the sum

    # Calculate the difference between the current sum and target number
    m = s - n

    # Check if the current sum equals the target
    if s == n:
        print(i)  # Print the current count i as the answer
        break  # Exit the loop

    # Check if the current sum exceeds the target
    if s > n:
        # Check if the difference is an even number
        if m % 2 == 0:
            print(i)  # Print the current count i as the answer
            break  # Exit the loop

    # Increment the counter to include the next integer
    i += 1
