def countSemiPrimes(t):
    total_semi_primes = 0  # Initialize the count of semi-primes to 0

    for i in range(1, t + 1):  # Iterate through each number from 1 to t
        divisor_count = 0
        current_number = i  # Set the current number to i

        for j in range(2, i):  # Check for divisors from 2 to i-1
            if current_number % j == 0:  # If j is a divisor of current_number
                divisor_count += 1  # Increment the divisor count
                while current_number % j == 0:  # While j is a divisor
                    current_number //= j  # Divide current_number by j

        # After counting the divisors, check if there are 2 distinct prime factors
        if divisor_count == 2:
            total_semi_primes += 1  # Increment total semi-primes

    return total_semi_primes  # Return the count of semi-prime numbers


# Test cases
print(countSemiPrimes(10))  # Example expected output: 4 (semi-primes are 4, 6, 9, 10)
print(countSemiPrimes(20))  # To check with a higher range
print(countSemiPrimes(1))   # Edge case, expected output: 0 (no semi-primes)
print(countSemiPrimes(30))  # General test case
