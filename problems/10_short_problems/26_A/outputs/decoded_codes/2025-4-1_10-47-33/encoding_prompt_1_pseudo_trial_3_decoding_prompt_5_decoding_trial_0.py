def count_semi_prime_numbers():
    # Read the upper limit integer value
    upper_limit = int(input())
    
    # Initialize the count of semi-prime numbers
    result = 0
    
    # Iterate through each integer from 1 to upper_limit (inclusive)
    for i in range(1, upper_limit + 1):
        count_divisors = 0  # Initialize count of distinct prime factors
        current_number = i   # Copy the value of i for manipulation
        
        # Check for prime factors from 2 to i - 1
        for j in range(2, i):
            if current_number % j == 0:  # If j is a divisor of current_number
                count_divisors += 1  # Found a new prime factor
                # Factor out all instances of j
                while current_number % j == 0:
                    current_number //= j
        
        # Check if the number of distinct prime factors is exactly 2
        if count_divisors == 2:
            result += 1  # i is a semi-prime number
    
    # Output the total count of semi-prime numbers found
    print(result)

# Example usage
# count_semi_prime_numbers()  # Uncomment to run the function and test
