def count_numbers_with_two_distinct_prime_factors():
    # Initialize the total number of test cases
    t = int(input())
    
    # Variable to store the count of numbers with exactly two distinct prime factors
    result = 0
    
    for i in range(1, t + 1):  # Loop through numbers from 1 to t
        count_of_distinct_primes = 0  # Count of distinct prime factors
        current_number = i  # The current number to factor
        
        # Check for all potential prime factors
        for j in range(2, i):  # Potential divisors from 2 to i-1
            if current_number % j == 0:  # If j is a factor of current_number
                count_of_distinct_primes += 1  # Found a distinct prime factor
                
                # Factor out j completely from current_number
                while current_number % j == 0:
                    current_number //= j
        
        # Check if the current number has exactly two distinct prime factors
        if count_of_distinct_primes == 2:
            result += 1  # Increment the result count
    
    # Output the final count of numbers with exactly two distinct prime factors
    print(result)

# Example of how to call the function
# count_numbers_with_two_distinct_prime_factors()  # Uncomment to execute
