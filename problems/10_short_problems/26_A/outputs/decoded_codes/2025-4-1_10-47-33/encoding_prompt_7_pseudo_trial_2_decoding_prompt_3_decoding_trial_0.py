def count_semi_primes(t):
    # Initialize the count of semi-primes
    total_semi_primes = 0

    # Iterate through each number from 1 to t
    for i in range(1, t + 1):
        divisor_count = 0
        current_number = i
        
        # Check for each number j from 2 to i-1
        for j in range(2, i):
            # Check if current_number is divisible by j
            if current_number % j == 0:
                divisor_count += 1
                
                # Divide current_number by j as long as it is divisible
                while current_number % j == 0:
                    current_number //= j
            
            # If we have already found 2 distinct divisors, we can break early
            if divisor_count > 2:
                break
        
        # If the count of distinct prime factors is exactly 2, it's a semi-prime
        if divisor_count == 2:
            total_semi_primes += 1

    return total_semi_primes

# Example usage:
# t = int(input())
# print(count_semi_primes(t))
