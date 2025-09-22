def count_semi_primes(t):
    # Initialize a variable to store the count of semi-prime numbers
    semi_prime_count = 0
    
    # Loop through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        # Initialize a counter for the number of distinct prime factors
        distinct_prime_count = 0
        current_number = i
        
        # Loop through possible factors from 2 to one less than the current number
        for j in range(2, current_number):
            # Check if j is a factor of current_number
            if current_number % j == 0:
                distinct_prime_count += 1  # Increment distinct prime factors count
                
                # Divide current_number by j until it is no longer divisible by j
                while current_number % j == 0:
                    current_number //= j  # Use integer division
                
        # If the number has exactly two distinct prime factors, count it as a semi-prime
        if distinct_prime_count == 2:
            semi_prime_count += 1
            
    # Return the total count of semi-prime numbers found
    return semi_prime_count

# Get the input value for t
t = int(input())
result = count_semi_primes(t)
print(result)
