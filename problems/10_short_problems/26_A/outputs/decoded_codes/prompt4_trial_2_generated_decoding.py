def is_semiprime(n):
    """Check if the number has exactly two distinct prime factors."""
    prime_factors = 0
    current_number = n
    
    for potential_factor in range(2, n):
        if current_number % potential_factor == 0:
            prime_factors += 1
            
            # Divide out all occurrences of potential_factor
            while current_number % potential_factor == 0:
                current_number //= potential_factor
                
        # If we have already found two distinct prime factors, we can stop
        if prime_factors > 2:
            return False
            
    # Return True if exactly two distinct prime factors were found
    return prime_factors == 2

def count_semiprimes(test_cases):
    """Count semiprime numbers from 1 to the given number of test cases."""
    result_count = 0
    
    for number in range(1, test_cases + 1):
        if is_semiprime(number):
            result_count += 1
            
    return result_count

# Read the number of test cases
test_cases = int(input())

# Get the count of semiprime numbers
semiprime_count = count_semiprimes(test_cases)

# Output the total count of semiprime numbers
print(semiprime_count)
