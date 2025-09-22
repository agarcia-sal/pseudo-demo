# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Read an integer from input representing the upper limit
    upper_limit = int(input())
    
    # Initialize the count of numbers with exactly two distinct prime factors
    total_count = 0
    
    # Loop through each number from 1 to upper_limit
    for current_number in range(1, upper_limit + 1):
        distinct_prime_count = 0  # Track the number of distinct prime factors
        current_value = current_number  # Value to be checked for prime factors
        
        # Check for potential prime factors from 2 to current_number - 1
        for potential_prime in range(2, current_number):
            # Check if potential_prime is a factor of current_value
            if current_value % potential_prime == 0:
                distinct_prime_count += 1  # Found a new distinct prime factor
                
                # Divide current_value by potential_prime to reduce it
                while current_value % potential_prime == 0:
                    current_value //= potential_prime
            
            # If we have found more than 2 distinct primes, break early
            if distinct_prime_count > 2:
                break

        # Check if we have exactly two distinct prime factors
        if distinct_prime_count == 2:
            total_count += 1  # Increment total count

    # Output the total count of numbers with exactly two distinct prime factors
    print(total_count)

# Call the function to execute the count
count_numbers_with_two_distinct_prime_factors()
