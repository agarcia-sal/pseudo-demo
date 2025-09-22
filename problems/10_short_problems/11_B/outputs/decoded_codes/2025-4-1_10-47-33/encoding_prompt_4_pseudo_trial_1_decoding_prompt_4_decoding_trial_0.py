def absolute_value(num):
    """Return the absolute value of the given number."""
    return -num if num < 0 else num

def sum_of_first_i_numbers(i):
    """Calculate the sum of the first i natural numbers."""
    return (i * (i + 1)) // 2  # Using integer division for whole numbers

# Start by taking the absolute value of user input and convert it to an integer
n = absolute_value(int(input()))

# Initialize a variable to keep track of the current number
i = 0

# Start an infinite loop for finding the required number
while True:
    # Calculate the sum of the first i natural numbers
    s = sum_of_first_i_numbers(i)

    # Determine how much s exceeds n
    m = s - n

    # Check if the sum equals n
    if s == n:
        print(i)  # Print the current number i
        break  # Stop the loop

    # Check if the sum exceeds n
    elif s > n:
        # Check if the difference m is even
        if m % 2 == 0:
            print(i)  # Print the current number i
            break  # Stop the loop

    # Increment i for the next iteration
    i += 1
