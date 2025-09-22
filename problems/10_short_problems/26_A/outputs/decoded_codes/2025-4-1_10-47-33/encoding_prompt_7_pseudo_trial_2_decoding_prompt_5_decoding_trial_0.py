def count_semi_primes(t):
    # Initialize the count of semi-prime numbers
    total_semi_primes = 0
    
    # Iterate through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize the count of distinct prime factors
        divisor_count = 0
        current_number = i
        
        # Check for divisors from 2 to i-1
        for j in range(2, i):
            # Check if j is a divisor of current_number
            if current_number % j == 0:
                # Increment the count of distinct prime factors
                divisor_count += 1
                
                # Divide current_number by j as long as it is divisible
                while current_number % j == 0:
                    current_number //= j
        
        # If there are exactly 2 distinct prime factors, it's a semi-prime
        if divisor_count == 2:
            total_semi_primes += 1

    # Return the total count of semi-prime numbers found
    return total_semi_primes

# Test case examples
# print(count_semi_primes(10))  # Example Test Case: Should return 2 (The semi-primes within 10 are 4 and 9)
# print(count_semi_primes(1))   # Test case for edge case: Should return 0 (No semi-primes below or equal to 1)
# print(count_semi_primes(20))  # Example Test Case: Should return the count of semi-primes within 20
