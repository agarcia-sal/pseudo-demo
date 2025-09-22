# Read an integer input, ensuring it is non-negative
n = abs(int(input()))

# Initialize a counter variable
i = 0

# Loop indefinitely
while True:
    # Calculate the sum of the first 'i' natural numbers
    s = (i * (i + 1)) / 2

    # Calculate the difference between the sum and the input number
    m = s - n

    # Check if the sum equals the input number
    if s == n:
        print(i)  # Output the current counter
        break  # Exit loop

    # Check if the sum exceeds the input number
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Output the current counter
            break  # Exit loop

    # Increment the counter for the next iteration
    i += 1
