def count_prime_numbers():
    # Input the upper limit for counting potential prime numbers
    t = int(input())
    
    # Initialize result variable to hold the count of prime numbers
    prime_count = 0
    
    # Loop through all numbers from 1 to t (inclusive)
    for i in range(1, t + 1):
        # Initialize a counter for distinct prime factors
        distinct_factors_count = 0
        num = i  # Number to be checked for prime factors
        
        # Loop through potential factors from 2 to i-1
        for j in range(2, i):
            # Check if j is a factor of num
            if num % j == 0:
                # Increment the count for distinct prime factors
                distinct_factors_count += 1
                
                # Remove all occurrences of the factor j from num
                while num % j == 0:
                    num //= j
        
        # If i has exactly two distinct prime factors, count it as prime
        if distinct_factors_count == 2:
            prime_count += 1
    
    # Output the total count of prime numbers
    print(prime_count)

# Uncomment below to test the function
# count_prime_numbers()  # Make sure to call the function to run the code
