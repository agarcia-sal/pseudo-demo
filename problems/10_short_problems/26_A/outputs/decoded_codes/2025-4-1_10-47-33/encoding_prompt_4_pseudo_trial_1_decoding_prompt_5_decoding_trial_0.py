def count_numbers_with_two_prime_factors():
    # Read integer input
    t = int(input())
    # Initialize result variable to count numbers with exactly two distinct prime factors
    result = 0
    
    # Loop through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        # Initialize count of distinct prime factors
        count = 0
        # Set number to the current value of i
        number = i
        
        # Check for prime factors from 2 to i-1
        for j in range(2, i):
            if number % j == 0:  # If j is a factor of number
                count += 1  # Increment the count of distinct prime factors
                # Keep dividing number by j while it's divisible
                while number % j == 0:
                    number //= j
        
        # Check if we found exactly two distinct prime factors
        if count == 2:
            result += 1  # Increment the result count
    
    # Output the final result
    print(result)

# Function call (if needed for testing purposes)
# count_numbers_with_two_prime_factors()
