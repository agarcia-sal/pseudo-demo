def count_numbers_with_two_distinct_prime_factors():
    # Read the integer input for the number of test cases
    test_cases = int(input())
    
    # Initialize a variable to hold the count of numbers with exactly two distinct prime factors
    result_count = 0
    
    # Iterate through each integer from 1 to test_cases
    for i in range(1, test_cases + 1):
        # Initialize a counter for distinct prime factors
        distinct_prime_count = 0
        current_number = i
        
        # Check for factors starting from 2 up to i
        for j in range(2, i + 1):
            # If j is a factor of current_number
            if current_number % j == 0:
                # Increment the distinct prime factor count
                distinct_prime_count += 1
                
                # Divide current_number by j until it is no longer divisible
                while current_number % j == 0:
                    current_number //= j
                
        # If there are exactly two distinct prime factors
        if distinct_prime_count == 2:
            result_count += 1
    
    # Output the final count of numbers with exactly two distinct prime factors
    print(result_count)

# Call the function to execute the program
count_numbers_with_two_distinct_prime_factors()
