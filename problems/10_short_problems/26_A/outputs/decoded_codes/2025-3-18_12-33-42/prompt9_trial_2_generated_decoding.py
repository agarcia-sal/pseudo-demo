# Function to count semiprime numbers up to a given max number
def count_semiprimes():
    # Get the maximum number to check for semiprimes
    max_number = int(input())
    
    # Initialize the semiprime counter
    semiprime_count = 0
    
    # Loop through each number from 1 to max_number
    for current_number in range(1, max_number + 1):
        # Initialize prime factor count
        prime_factor_count = 0
        
        # Set temporary number to current number
        temporary_number = current_number
        
        # Check for prime factors
        for potential_factor in range(2, current_number):
            # If potential_factor divides temporary_number
            if temporary_number % potential_factor == 0:
                prime_factor_count += 1
                
                # Reduce temporary_number by dividing it by potential_factor
                while temporary_number % potential_factor == 0:
                    temporary_number //= potential_factor
        
        # Check if the number is a semiprime
        if prime_factor_count == 2:
            semiprime_count += 1
    
    # Output the result
    print(semiprime_count)

# Execute the function
count_semiprimes()
