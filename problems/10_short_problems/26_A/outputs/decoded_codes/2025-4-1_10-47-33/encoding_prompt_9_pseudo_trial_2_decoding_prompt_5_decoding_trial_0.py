# Function to count and output the number of prime numbers up to a specified integer
def count_primes_up_to_maximum():
    # Get user input for the maximum number
    maximum_number = int(input())
    
    # Initialize count of prime numbers
    prime_count = 0
    
    # Loop through each number from 1 to maximum_number
    for current_number in range(1, maximum_number + 1):
        # Initialize factor count for the current number
        factor_count = 0
        remaining_number = current_number
        
        # Check for factors from 2 to one less than current_number
        for potential_factor in range(2, current_number):
            if remaining_number % potential_factor == 0:
                factor_count += 1
                # Remove the factor from remaining_number
                while remaining_number % potential_factor == 0:
                    remaining_number //= potential_factor
        
        # Identify if current_number is prime
        if factor_count == 1:  # A prime number has exactly one factor (itself) in our context
            prime_count += 1
    
    # Output the total number of prime numbers found
    print(prime_count)

# Example test case (uncomment to test)
# count_primes_up_to_maximum()  # For input 10, should output 4 (2, 3, 5, 7)
