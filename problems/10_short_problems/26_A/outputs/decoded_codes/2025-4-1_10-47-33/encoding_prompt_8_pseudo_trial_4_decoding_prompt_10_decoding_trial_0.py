def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_product_of_two_primes(total_numbers):
    """Count how many numbers between 1 and total_numbers are products of exactly two prime numbers."""
    result = 0  # Initialize the count of numbers that meet criteria
    
    for current_number in range(1, total_numbers + 1):
        prime_factor_count = 0  # Reset the count of distinct prime factors
        
        # Temporary number to manipulate
        temp_number = current_number
        
        # Check for potential prime factors starting from 2
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:
                if is_prime(potential_factor):
                    prime_factor_count += 1  # Found a new prime factor
                    
                    # Remove all occurrences of this prime factor from temp_number
                    while temp_number % potential_factor == 0:
                        temp_number //= potential_factor

        # Check if we found exactly two distinct prime factors
        if prime_factor_count == 2:
            result += 1  # Increment the result count
            
    return result  # Return the final count

def main():
    total_numbers = int(input())  # Read an integer input from the user
    result = count_numbers_product_of_two_primes(total_numbers)  # Get the count
    print(result)  # Output the result

if __name__ == "__main__":
    main()  # Start the program
