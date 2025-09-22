def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    divisor_count = 0  # Initialize divisor count

    # Check for divisibility from 2 to number - 1
    for potential_divisor in range(2, number):
        if number % potential_divisor == 0:
            divisor_count += 1  # Increment divisor count
            # Remove all occurrences of potential_divisor from number
            while number % potential_divisor == 0:
                number //= potential_divisor

    return divisor_count == 1  # A prime number has exactly one divisor besides itself

def main():
    # Get input from user
    t = int(input())
    prime_count = 0  # Counter for prime numbers

    # Loop through each number from 1 to t
    for current_number in range(1, t + 1):
        if is_prime(current_number):
            prime_count += 1  # Increment prime count if current number is prime

    # Output the total count of prime numbers found
    print(prime_count)

# Execute the main function
if __name__ == "__main__":
    main()
