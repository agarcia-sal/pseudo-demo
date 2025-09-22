def count_numbers_with_two_distinct_prime_factors():
    # Read the input value
    input_number = int(input())
    
    # Initialize a variable to count the desired numbers
    count_of_numbers = 0
    
    # Loop through each number from 1 to input_number
    for current_number in range(1, input_number + 1):
        # Initialize a counter to track the number of distinct prime factors
        distinct_prime_count = 0
        
        # Create a variable to work with current_number
        working_number = current_number
        
        # Check for prime factors starting from 2 up to current_number - 1
        for potential_factor in range(2, current_number):
            # If potential_factor is a factor of working_number
            if working_number % potential_factor == 0:
                # Increase the count of distinct prime factors
                distinct_prime_count += 1
                
                # Divide working_number by potential_factor until it is no longer divisible
                while working_number % potential_factor == 0:
                    working_number //= potential_factor
        
        # Check if the number has exactly two distinct prime factors
        if distinct_prime_count == 2:
            # Increase the overall count of such numbers
            count_of_numbers += 1
            
    # Output the result, which is the count of numbers with exactly two distinct prime factors
    print(count_of_numbers)

# Example of testing the function
# The following call is for testing purposes and can be uncommented when running the code.
# count_numbers_with_two_distinct_prime_factors()
