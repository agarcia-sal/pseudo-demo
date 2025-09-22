# BEGIN

# Read and convert input to an absolute integer
number = abs(int(input()))

# Initialize index variable
index = 0

# Infinite loop to find the solution
while True:
    # Calculate the sum of first 'index' natural numbers
    sum_n = (index * (index + 1)) // 2  # Using integer division

    # Calculate the difference between sum and number
    difference = sum_n - number

    # Check if the sum equals the number
    if sum_n == number:
        print(index)  # Print the index if condition met
        break

    # Check if the sum is greater than the number
    elif sum_n > number:
        # Check if the difference is even
        if difference % 2 == 0:  # Checking if the difference is even
            print(index)  # Print the index if condition met
            break

    # Increment the index for the next iteration
    index += 1

# END
