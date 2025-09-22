def count_semiprimes(limit):
    """Counts how many semiprime numbers exist from 1 to the given limit."""
    semiprime_count = 0  # Initialize the count of semiprimes

    for i in range(1, limit + 1):  # Loop through each number from 1 to limit
        divisor_count = 0  # Initialize count of distinct prime divisors
        current_number = i  # Keep track of the current number

        # Check for potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            if current_number % potential_divisor == 0:  # Check if divisible
                divisor_count += 1  # Found a divisor
                # Reduce current_number by dividing by potential_divisor
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor
        
        # A semiprime has exactly two distinct prime factors
        if divisor_count == 2:
            semiprime_count += 1  # Increment semiprime count
    
    return semiprime_count  # Return the total count of semiprimes

# Read an integer value from the user
input_limit = int(input())  
output = count_semiprimes(input_limit)  # Get the count of semiprimes
print(output)  # Print the result
