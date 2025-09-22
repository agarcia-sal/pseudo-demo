def count_numbers_with_two_distinct_prime_factors():
    # Read the upper limit for checking numbers
    t = int(input())
    
    # Initialize a variable to count how many numbers have exactly two distinct prime factors
    result = 0
    
    # Check each number from 1 to t
    for i in range(1, t + 1):
        count = 0  # Count of distinct prime factors
        number = i  # Temporary variable for factorization
        
        # Check for factors from 2 to i - 1
        for j in range(2, i):
            if number % j == 0:  # j is a factor of number
                count += 1  # Found a distinct prime factor
                
                # Remove the factor completely
                while number % j == 0:
                    number //= j
        
        # Check if we found exactly two distinct prime factors
        if count == 2:
            result += 1  # Increment the result count
            
    # Print the total count of numbers with exactly two distinct prime factors
    print(result)

# Call the function to execute the program
count_numbers_with_two_distinct_prime_factors()
