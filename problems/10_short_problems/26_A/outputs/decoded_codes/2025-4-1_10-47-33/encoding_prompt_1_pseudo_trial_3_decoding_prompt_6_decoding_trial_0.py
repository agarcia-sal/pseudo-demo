# Start of the code

# Step 2: Input - Read the upper limit as an integer
upper_limit = int(input())

# Step 3: Initialize result to 0 for counting semi-prime numbers
semi_prime_count = 0

# Step 4: Loop through each integer from 1 to upper_limit (inclusive)
for number in range(1, upper_limit + 1):
    # Step 4.1: Initialize countDivisors to 0 for counting distinct prime factors
    distinct_prime_count = 0
    # Step 4.2: Set currentNumber to number for manipulation
    current_number = number
    
    # Step 4.3: Loop for each integer from 2 to (number - 1)
    for divisor in range(2, number):
        # Step 4.3.1: Check if currentNumber is divisible by divisor
        if current_number % divisor == 0:
            # Increment count of distinct prime factors
            distinct_prime_count += 1
            
            # Step 4.3.1.1: While currentNumber is divisible by divisor, continue dividing
            while current_number % divisor == 0:
                current_number //= divisor  # Use floor division to keep it integer
            
    # Step 4.4: If we found exactly 2 distinct prime factors, it's a semi-prime
    if distinct_prime_count == 2:
        semi_prime_count += 1  # Increment the semi-prime count

# Step 5: Output the total count of semi-prime numbers found
print(semi_prime_count)

# End of the code
