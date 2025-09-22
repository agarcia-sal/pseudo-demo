# Read input
upper_limit = int(input())

# Initialize counter
prime_count = 0

# Loop through each number
for current_number in range(1, upper_limit + 1):
    divisor_count = 0
    temp_number = current_number

    # Check for divisors
    for potential_divisor in range(2, current_number):
        if temp_number % potential_divisor == 0:
            divisor_count += 1
            while temp_number % potential_divisor == 0:
                temp_number /= potential_divisor

    # Determine if prime
    if divisor_count == 1:
        prime_count += 1

# Output result
print(prime_count)
