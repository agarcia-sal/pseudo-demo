def count_semi_primes(limit):
    semi_prime_count = 0  # Counter for semi-primes

    for current_number in range(1, limit + 1):
        divisor_count = 0  # Counter for unique prime factors
        number = current_number

        # Check for divisors from 2 to current_number - 1
        for divisor in range(2, current_number):
            if number % divisor == 0:  # Found a divisor
                divisor_count += 1  # Increment the count of unique prime factors
                # Divide out all occurrences of this divisor from number
                while number % divisor == 0:
                    number //= divisor  # Reduce the number by the found divisor
                
            # Early exit if we have found 2 unique primes
            if divisor_count > 2:
                break

        # A semi-prime has exactly two unique prime factors
        if divisor_count == 2:
            semi_prime_count += 1  # Increase semi-prime count

    return semi_prime_count  # Output the count of semi-primes


# Main program execution
t = int(input())  # Take input from the user
print(count_semi_primes(t))  # Output the count of semi-primes
