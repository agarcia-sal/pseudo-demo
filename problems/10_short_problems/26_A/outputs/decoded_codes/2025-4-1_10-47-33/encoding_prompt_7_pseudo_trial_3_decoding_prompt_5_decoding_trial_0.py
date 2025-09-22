def count_semi_primes(limit):
    # Initialize the count of semiprime numbers
    semiprime_count = 0
    
    # Iterate through each number from 1 to the specified limit
    for i in range(1, limit + 1):
        # Initialize the count of divisors for the current number
        divisor_count = 0
        current_number = i
        
        # Check potential divisors from 2 up to (i - 1)
        for potential_divisor in range(2, i):
            # Check if current_number is divisible by the potential_divisor
            if current_number % potential_divisor == 0:
                # Increment the divisor count
                divisor_count += 1
                
                # Remove factors of potential_divisor from current_number
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor

        # If exactly two distinct prime factors were found, it's a semiprime
        if divisor_count == 2:
            semiprime_count += 1
            
    return semiprime_count

# Get the input limit from the user
input_limit = int(input())
# Count semiprimes up to the input limit
output = count_semi_primes(input_limit)
# Print the result
print(output)
