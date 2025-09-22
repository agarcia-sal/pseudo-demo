# Step 1: Get input from the user and store it in an integer variable
t = int(input())

# Step 2: Initialize a counter for prime numbers
prime_count = 0

# Step 3: Loop through each number from 1 to t (inclusive)
for current_number in range(1, t + 1):
    # Initialize the divisor count and remaining value
    divisor_count = 0
    remaining_value = current_number
    
    # Step 4: Check for potential divisors from 2 to current_number - 1
    for potential_divisor in range(2, current_number):
        # Check if remaining_value is divisible by potential_divisor
        if remaining_value % potential_divisor == 0:
            # If divisible, increment the divisor count
            divisor_count += 1
            # Remove all occurrences of potential_divisor from remaining_value
            while remaining_value % potential_divisor == 0:
                remaining_value //= potential_divisor
    
    # Step 5: Determine if the current number is prime
    if divisor_count == 1 and current_number > 1:  # 1 has no prime factors and is not prime
        prime_count += 1  # Increment prime count if prime

# Step 6: Output the final count of prime numbers found
print(prime_count)
