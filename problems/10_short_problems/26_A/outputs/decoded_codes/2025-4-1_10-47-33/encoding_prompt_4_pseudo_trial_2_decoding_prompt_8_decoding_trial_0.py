# Read the integer input for the number of test cases
test_cases = int(input())

# Initialize the result counter to zero
result_count = 0

# Iterate through each number from 1 to the number of test cases
for i in range(1, test_cases + 1):
    # Initialize a counter for prime factors
    prime_factor_count = 0
    num = i
    factors = set()  # To track distinct prime factors
    
    # Check for factors from 2 to i - 1
    for j in range(2, i):
        # Only check if j is a factor
        if num % j == 0:
            # Track distinct prime factor
            factors.add(j)

            # Divide num by j until it is no longer divisible
            while num % j == 0:
                num //= j
    
    # If the number has exactly two distinct prime factors
    if len(factors) == 2:
        # Increment the result count for numbers with two prime factors
        result_count += 1

# Output the total count of numbers with exactly two prime factors
print(result_count)
