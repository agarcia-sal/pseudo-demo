# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Read the upper limit integer value
    upper_limit = int(input())
    
    # Initialize result variable to count qualifying numbers
    result = 0
    
    # Loop through each number from 1 to upper_limit (inclusive)
    for number in range(1, upper_limit + 1):
        # Initialize count of distinct prime factors
        distinct_prime_count = 0
        temp_number = number
        
        # Check for prime factors starting from 2
        for potential_prime in range(2, temp_number):
            # Check if potential_prime is a factor of temp_number
            if temp_number % potential_prime == 0:
                distinct_prime_count += 1  # Found a distinct prime factor
                
                # Remove this prime factor completely from temp_number
                while temp_number % potential_prime == 0:
                    temp_number //= potential_prime
        
        # If the count of distinct prime factors is exactly 2
        if distinct_prime_count == 2:
            result += 1  # Increment result count
    
    # Output the final count of numbers with exactly two distinct prime factors
    print(result)

# Call the function
count_numbers_with_two_distinct_prime_factors()
