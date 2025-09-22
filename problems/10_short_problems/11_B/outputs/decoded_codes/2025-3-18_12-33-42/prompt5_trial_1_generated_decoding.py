# This code determines the largest integer 'i' such that the sum of the first 'i' integers
# equals or surpasses a given absolute value 'n', checking if the excess can be evenly divided by 2.

# Get absolute value of the integer input from the user
n = abs(int(input()))

# Initialize the counter for integers to be summed
i = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'i' integers
    s = (i * (i + 1)) // 2  # Using integer division for the sum

    # Calculate the difference between the sum and input 'n'
    m = s - n

    # Check if the sum 's' is equal to 'n'
    if s == n:
        print(i)  # Print the integer 'i'
        break  # Exit the loop

    # Check if the sum 's' is greater than 'n'
    elif s > n:
        # Check if the difference 'm' is even
        if m % 2 == 0:
            print(i)  # Print the integer 'i'
            break  # Exit the loop

    # Increment 'i' to consider the next integer in the next iteration
    i += 1
