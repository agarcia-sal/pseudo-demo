def count_semiprimes():
    # Get the upper limit for counting semiprimes from user input
    upper_limit = int(input())
    
    # Initialize the semiprime counter
    semiprime_count = 0
    
    # Loop through each number from 1 to the upper limit
    for current_number in range(1, upper_limit + 1):
        prime_factor_count = 0  # Reset the prime factor count for the current number
        divided_number = current_number
        
        # Identify prime factors for the current number
        for possible_factor in range(2, current_number):
            if divided_number % possible_factor == 0:  # Check if possible_factor is a divisor
                prime_factor_count += 1  # Found a prime factor
                # Divide out all instances of this factor
                while divided_number % possible_factor == 0:
                    divided_number //= possible_factor
        
        # Check if the current number is a semiprime (exactly 2 distinct prime factors)
        if prime_factor_count == 2:
            semiprime_count += 1  # Increment the semiprime counter
    
    # Output the total count of semiprimes
    print(semiprime_count)

# Example of how to run the function
# count_semiprimes()  # Uncomment this line to run the function
