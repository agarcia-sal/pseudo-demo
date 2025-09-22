def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    divisor_count = 0
    original_number = number
    
    # Check for divisors from 2 up to but not including original_number
    for divisor in range(2, original_number):
        if original_number % divisor == 0:
            # If divisible, increment the divisor count
            divisor_count += 1
            # Reduce the number by dividing it by the divisor
            while original_number % divisor == 0:
                original_number //= divisor
        if divisor_count > 2:
            return False  # Early exit if more than 2 distinct divisors
    
    return divisor_count == 1  # There should be exactly one prime divisor which is the number itself

def main():
    # Read an integer input representing the number of tests
    test_count = int(input())
    
    # Initialize a result counter for prime numbers
    prime_count = 0
    
    # Loop through each number from 1 to test_count
    for number in range(1, test_count + 1):
        if is_prime(number):
            prime_count += 1  # Increment prime_count if the number is prime
    
    # Output the total count of prime numbers found
    print(prime_count)

# Entry point for the script
if __name__ == "__main__":
    main()
