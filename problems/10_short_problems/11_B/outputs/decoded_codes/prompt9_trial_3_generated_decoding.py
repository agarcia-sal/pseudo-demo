# Get Input
n = int(input())
if n < 0:  # Convert negative input to its absolute value
    n = abs(n)

# Initialize Counter
i = 0

# Loop until a condition is met
while True:
    # Calculate the sum of the first 'i' natural numbers
    sum_of_first_i = (i * (i + 1)) // 2  # Using integer division

    # Calculate the difference between the sum and n
    difference = sum_of_first_i - n

    # Check if the sum equals n
    if sum_of_first_i == n:
        print(i)  # Print the result and exit loop
        break

    # Check if the sum is greater than n
    if sum_of_first_i > n:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(i)  # Print the result and exit loop
            break

    # Increment the counter
    i += 1
