def count_semiprime_numbers():
    # Read the upper limit of the range
    upper_limit = int(input())
    
    # Initialize a variable to count semiprime numbers
    semiprime_count = 0

    # Loop through each number from 1 to upper_limit (inclusive)
    for current_number in range(1, upper_limit + 1):
        # Count how many distinct prime factors 'current_number' has
        distinct_prime_count = 0
        temp_number = current_number  

        # Check potential factors from 2 up to the current number
        for potential_factor in range(2, current_number):
            # Check if the potential factor divides the current number
            if temp_number % potential_factor == 0:
                # We found a new prime factor
                distinct_prime_count += 1
                
                # Remove all occurrences of potential_factor from temp_number
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # If we found exactly two distinct prime factors, it's a semiprime
        if distinct_prime_count == 2:
            semiprime_count += 1  # Increment the semiprime count

    # Print the total count of semiprime numbers found
    print(semiprime_count)

# Example test case
# When testing this function, make sure to input an integer through standard input 
# to see how many semiprimes are between 1 and the input number.
