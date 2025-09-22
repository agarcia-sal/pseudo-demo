def count_semiprimes(limit):
    semiprime_count = 0  # Initialize counter for semiprimes
    for i in range(1, limit + 1):  # Iterate from 1 to the limit inclusive
        divisor_count = 0  # Initialize divisor count for each number
        current_number = i  # Set current number to i
        for potential_divisor in range(2, i):  # Check for potential divisors
            if current_number % potential_divisor == 0:  # If divisible by potential divisor
                divisor_count += 1  # Increment divisor count
                while current_number % potential_divisor == 0:  # Keep dividing
                    current_number //= potential_divisor
        if divisor_count == 2:  # If exactly two distinct prime factors
            semiprime_count += 1  # Increment semiprime count
    return semiprime_count  # Return the total count of semiprimes

input_limit = int(input())  # Read the upper limit from user input
output = count_semiprimes(input_limit)  # Call the function with the input limit
print(output)  # Print the result
