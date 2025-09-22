# Read the integer input for the number of test cases
test_cases = int(input())

# Initialize the result counter to zero
result_count = 0

# Iterate through each number from 1 to the number of test cases
for i in range(1, test_cases + 1):
    # Initialize a counter for prime factors
    prime_factor_count = 0
    num = i
    
    # Check for factors from 2 to one less than the number
    for j in range(2, i):
        if num % j == 0:  # Check if divisor j is a factor of num
            # Increment the prime factor counter
            prime_factor_count += 1
            
            # Divide num by j until it is no longer divisible
            while num % j == 0:
                num = num // j  # Use integer division to update num

    # If the number has exactly two distinct prime factors
    if prime_factor_count == 2:
        # Increment the result count for numbers with two prime factors
        result_count += 1

# Output the total count of numbers with exactly two prime factors
print(result_count)
