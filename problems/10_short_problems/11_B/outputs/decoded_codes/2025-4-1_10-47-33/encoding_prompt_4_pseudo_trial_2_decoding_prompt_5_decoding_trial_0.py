# Read an integer input, ensuring it is non-negative
n = abs(int(input()))

# Initialize a counter variable
i = 0

# Loop indefinitely
while True:
    # Calculate the sum of the first 'i' natural numbers
    sum_natural_numbers = (i * (i + 1)) // 2

    # Calculate the difference between the sum and the input number
    difference = sum_natural_numbers - n

    # Check if the sum equals the input number
    if sum_natural_numbers == n:
        print(i)  # Output the current counter
        break

    # Check if the sum exceeds the input number
    elif sum_natural_numbers > n:
        # Check if the difference is even
        if difference % 2 == 0:
            print(i)  # Output the current counter
            break

    # Increment the counter for the next iteration
    i += 1
