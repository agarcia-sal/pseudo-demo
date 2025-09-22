# Function to count numbers that are products of exactly two distinct prime numbers
def count_distinct_prime_products():
    # Receive input for the limit
    limit = int(input())
    
    # Initialize count of valid products
    count_of_products = 0
    
    # Iterate through each number from 1 to limit
    for current_number in range(1, limit + 1):
        # Initialize the distinct prime factors counter
        distinct_prime_factors = 0
        # Temporary variable to factor the current number
        temporary_number = current_number
        
        # Check for prime factors
        for potential_prime in range(2, current_number):
            # Check if potential_prime is a factor
            if temporary_number % potential_prime == 0:
                distinct_prime_factors += 1
                # Remove all occurrences of this prime factor
                while temporary_number % potential_prime == 0:
                    temporary_number //= potential_prime
        
        # Check if there are exactly two distinct prime factors
        if distinct_prime_factors == 2:
            count_of_products += 1
    
    # Output the total count of products found
    print(count_of_products)

# Sample call (will prompt the user for an input)
count_distinct_prime_products()
