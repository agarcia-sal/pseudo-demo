def is_prime(num):
    """Determine if a number is prime."""
    if num < 2:
        return False
    for potential_factor in range(2, int(num**0.5) + 1):  # Optimized to check up to the square root
        if num % potential_factor == 0:
            return False
    return True

def main():
    # Get the number of test cases from user input
    test_case_count = int(input())
    
    # Initialize a result variable to store count of prime numbers
    prime_count = 0

    # Loop over each number from 1 to the value of test_case_count
    for current_number in range(1, test_case_count + 1):
        # Check if the current number is prime
        if is_prime(current_number):
            prime_count += 1
            
    # Output the count of prime numbers found
    print(prime_count)

if __name__ == "__main__":
    main()
