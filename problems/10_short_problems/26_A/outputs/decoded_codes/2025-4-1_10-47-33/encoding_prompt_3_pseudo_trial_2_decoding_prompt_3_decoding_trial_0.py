def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for potential_factor in range(2, int(num**0.5) + 1):
        if num % potential_factor == 0:
            return False
    return True

def count_primes():
    """Count prime numbers based on user input."""
    # Get the number of test cases from user input
    test_case_count = int(input())
    
    # Initialize a count for prime numbers
    prime_count = 0
    
    # Loop over each number from 1 to test_case_count
    for current_number in range(1, test_case_count + 1):
        # Check if the current number is prime
        if is_prime(current_number):
            prime_count += 1
            
    # Output the count of prime numbers found
    print(prime_count)

# Call the function to execute the program
count_primes()
