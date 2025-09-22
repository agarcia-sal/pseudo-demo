def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_products_of_two_primes(total_numbers):
    """Count how many numbers between 1 and total_numbers are products of exactly two prime numbers."""
    result = 0  # Initialize count

    for current_number in range(1, total_numbers + 1):
        prime_factor_count = 0  # Reset count for each number
        temp_number = current_number  # Work with a temporary number

        # Check for prime factors
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0 and is_prime(potential_factor):
                prime_factor_count += 1  # Found a new prime factor
                
                # Reduce temp_number by removing all occurrences of this factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # Check if exactly two distinct prime factors were found
        if prime_factor_count == 2:
            result += 1  # Increment the result

    return result

# Main entry point
if __name__ == "__main__":
    total_numbers = int(input())  # Get integer input from user
    result = count_products_of_two_primes(total_numbers)  # Count products of two primes
    print(result)  # Output the result
