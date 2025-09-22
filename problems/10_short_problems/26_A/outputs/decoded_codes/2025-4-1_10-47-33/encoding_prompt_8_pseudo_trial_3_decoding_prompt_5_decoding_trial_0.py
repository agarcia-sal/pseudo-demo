def count_semiprimes():
    # Get the input value for t
    t = int(input())
    
    # Initialize a variable to keep track of the count of semiprimes
    semiprime_count = 0
    
    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize a count for the number of distinct prime factors
        distinct_prime_count = 0
        # Copy the current number to a temporary variable for manipulation
        current_number = i
        
        # Check for factors starting from 2
        for j in range(2, current_number):
            # If j is a factor of the current_number
            if current_number % j == 0:
                # Increment the count of distinct prime factors
                distinct_prime_count += 1
                
                # Continue dividing current_number by j until it no longer divides evenly
                while current_number % j == 0:
                    current_number //= j
        
        # After checking all possible factors
        # If the number has exactly two distinct prime factors, it is a semiprime
        if distinct_prime_count == 2:
            # Increment the semiprime count
            semiprime_count += 1
    
    # Output the total count of semiprimes found
    print(semiprime_count)

# Example Test Case
# count_semiprimes() # Uncomment this line to test the function after providing input
