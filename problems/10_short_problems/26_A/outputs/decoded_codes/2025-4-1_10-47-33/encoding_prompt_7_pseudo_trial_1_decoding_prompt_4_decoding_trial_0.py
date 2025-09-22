def count_semi_primes(limit):
    semi_prime_count = 0  # Counter for semi-primes

    for number in range(1, limit + 1):
        divisor_count = 0  # Counter for distinct prime divisors
        current_number = number

        # Check for divisors from 2 up to current_number - 1
        for divisor in range(2, current_number):
            if current_number % divisor == 0:  # Found a divisor
                divisor_count += 1  # Increment divisor count

                # Divide out all occurrences of this divisor from current_number
                while current_number % divisor == 0:
                    current_number //= divisor  # Reduce current number

            # Early exit if we already found 2 distinct prime factors
            if divisor_count > 2:
                break
        
        # A semi-prime has exactly two unique prime factors
        if divisor_count == 2:
            semi_prime_count += 1  # Increase semi-prime count

    return semi_prime_count  # Output the count of semi-primes


# Main program execution
t = int(input())  # Get input from the user
result = count_semi_primes(t)  # Count semi-primes up to the input number
print(result)  # Print the result
