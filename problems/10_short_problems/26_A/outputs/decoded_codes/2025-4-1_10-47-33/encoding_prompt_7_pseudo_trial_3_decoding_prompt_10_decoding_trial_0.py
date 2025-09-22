def count_semiprimes(limit):
    """
    Count the number of semiprime numbers from 1 to the given limit.
    
    A semiprime is a natural number that is the product of exactly two prime numbers.
    """
    semiprime_count = 0  # Initialize the count of semiprime numbers

    # Iterate through each number from 1 to the limit
    for i in range(1, limit + 1):
        divisor_count = 0  # Initialize the count of unique prime divisors
        current_number = i  # Hold the current number being evaluated
        
        # Check each number from 2 to (current_number - 1)
        for potential_divisor in range(2, current_number):
            # If the current number is divisible by the potential divisor
            if current_number % potential_divisor == 0:
                divisor_count += 1  # We found a divisor
                # Divide out all occurrences of the potential divisor
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor
        
        # If we found exactly two unique prime divisors, it's a semiprime
        if divisor_count == 2:
            semiprime_count += 1
            
    return semiprime_count

# Read input from the user
input_limit = int(input())
# Call the function to count semiprimes and print the result
output = count_semiprimes(input_limit)
print(output)
