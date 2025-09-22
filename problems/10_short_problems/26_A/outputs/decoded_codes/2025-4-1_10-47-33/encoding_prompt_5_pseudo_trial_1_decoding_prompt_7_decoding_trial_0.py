def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(upper_limit):
    """Count the number of semiprime numbers up to the given limit."""
    
    # Initialize a counter to keep track of semiprime numbers found.
    semiprime_count = 0

    # Loop through each number from 1 to upper limit.
    for number in range(1, upper_limit + 1):
        prime_factor_count = 0  # Counter for counting distinct prime factors
        current_number = number  # Number currently being evaluated

        # Loop through all numbers starting from 2 up to the current number to check for factors.
        for potential_factor in range(2, current_number):
            # If the current number is divisible by the potential factor.
            if current_number % potential_factor == 0:
                # Check if potential_factor is prime
                if is_prime(potential_factor):
                    prime_factor_count += 1  # Increase the distinct prime factors count

                # Continuous division of current number by this factor.
                while current_number % potential_factor == 0:
                    current_number //= potential_factor
        
        # Check if exactly two distinct prime factors were found.
        if prime_factor_count == 2:
            semiprime_count += 1  # Found a semiprime number, increase the count

    return semiprime_count

# Main execution flow
if __name__ == "__main__":
    upper_limit = int(input())  # Take an integer input which represents the upper limit
    semiprime_count = count_semiprimes(upper_limit)  # Count semiprime numbers
    print(semiprime_count)  # Output the total count of semiprime numbers found
