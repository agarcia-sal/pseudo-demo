# Read the integer input for the number of test cases
test_cases = int(input())

# Initialize the result counter to zero
result_count = 0

# Iterate through each number from 1 to the number of test cases
for i in range(1, test_cases + 1):
    # Initialize a counter for prime factors
    prime_factor_count = 0
    num = i
    
    # Set to keep track of distinct prime factors
    distinct_prime_factors = set()
    
    # Check for factors from 2 to num
    for j in range(2, num + 1):
        # Check if j is a factor of num
        while num % j == 0:
            # If j is a new prime factor, add to the set
            distinct_prime_factors.add(j)
            # Divide num by j
            num //= j
            
        # If we already found two prime factors, no need to continue
        if len(distinct_prime_factors) > 2:
            break

    # If the number has exactly two distinct prime factors
    if len(distinct_prime_factors) == 2:
        # Increment the result count for numbers with two prime factors
        result_count += 1

# Output the total count of numbers with exactly two prime factors
print(result_count)
