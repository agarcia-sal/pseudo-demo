# Step 1: Read an integer value t from user input
upper_limit = int(input())

# Step 2: Initialize result variable to count numbers with exactly two distinct prime factors
count_result = 0

# Step 3: Iterate through each integer from 1 to t (inclusive)
for current_integer in range(1, upper_limit + 1):
    # Step 4: Initialize count to track distinct prime factors
    distinct_prime_count = 0
    current_number = current_integer  # Store the current integer to manipulate for prime factorization
    
    # Step 5: Check for factors starting from 2 to the current integer - 1
    for potential_prime in range(2, current_integer):
        # Check if current_number is divisible by potential_prime
        if current_number % potential_prime == 0:
            # Increment the distinct prime factor count
            distinct_prime_count += 1
            
            # Remove all occurrences of the potential prime from current_number
            while current_number % potential_prime == 0:
                current_number //= potential_prime  # Use integer division to divide
            
    # Step 6: Check if exactly two distinct prime factors were found
    if distinct_prime_count == 2:
        count_result += 1  # Increment the result counter

# Step 7: Output the result
print(count_result)
