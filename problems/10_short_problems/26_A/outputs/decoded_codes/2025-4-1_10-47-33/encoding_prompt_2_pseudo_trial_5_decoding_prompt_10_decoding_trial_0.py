def count_primes(total_numbers):
    prime_count = 0  # This will keep track of how many prime numbers are found.

    # Iterate through each number from 1 to total_numbers (inclusive).
    for current_number in range(1, total_numbers + 1):
        divisor_count = 0  # Reset the divisor count for the current number.
        numerator = current_number  # The number to check for primality.

        # Check potential divisors starting from 2 up to (but not including) current_number
        for potential_divisor in range(2, current_number):
            if numerator % potential_divisor == 0:  # Check if divisible
                divisor_count += 1  # Increment divisor count

                # Remove all factors of potential_divisor from numerator
                while numerator % potential_divisor == 0:
                    numerator //= potential_divisor
        
        # Check if the number is prime (exactly 2 distinct divisors)
        if divisor_count == 2:
            prime_count += 1  # Increment the prime count

    return prime_count  # Return the total number of prime numbers found

# Run the function with input obtained from the user
if __name__ == "__main__":
    total_numbers = int(input())  # Receive input from the user
    print(count_primes(total_numbers))  # Output the result
