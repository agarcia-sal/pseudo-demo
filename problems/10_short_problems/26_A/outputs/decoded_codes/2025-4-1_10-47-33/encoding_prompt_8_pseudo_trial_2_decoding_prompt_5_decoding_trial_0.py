# Function to count semiprime numbers up to a given limit
def count_semiprimes():
    # Read the integer limit from user input
    limit = int(input())
    
    # Initialize counter for semiprime numbers
    semiprime_count = 0

    # Loop through each number from 1 to limit (inclusive)
    for current_number in range(1, limit + 1):
        # Initialize counter for prime factors
        prime_factor_count = 0
        # Temporary number for factorization
        temp_number = current_number

        # Check potential factors starting from 2
        for potential_factor in range(2, current_number):
            # If potential_factor divides the current_number
            if temp_number % potential_factor == 0:
                # Increment the prime factor count
                prime_factor_count += 1
                
                # Divide temp_number by potential_factor while it's divisible
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # If there are exactly two prime factors, it is a semiprime
        if prime_factor_count == 2:
            semiprime_count += 1  # Increment the semiprime count

    # Output the total count of semiprime numbers found
    print(semiprime_count)

# Function call to execute the semiprime counting
count_semiprimes()
