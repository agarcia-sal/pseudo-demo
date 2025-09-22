def count_semiprimes():
    # Read an integer t from the user, representing the upper limit
    t = int(input())
    
    # Initialize a count variable to keep track of semiprimes found
    semiprime_count = 0
    
    # Loop through each number from 1 to t (inclusive)
    for current_number in range(1, t + 1):
        distinct_prime_count = 0  # Counter for distinct prime factors
        number = current_number
        
        # Loop through potential factors starting at 2
        for potential_factor in range(2, current_number):
            if number % potential_factor == 0:  # Check divisibility
                distinct_prime_count += 1  # Found a new distinct prime factor
                
                # Reduce number by its prime factor
                while number % potential_factor == 0:
                    number //= potential_factor
        
        # After checking all potential factors, check the distinct prime count
        if distinct_prime_count == 2:
            semiprime_count += 1  # A semiprime was found
    
    # Output the value of semiprime_count
    print(semiprime_count)

# The function can be called to execute the program
count_semiprimes()
