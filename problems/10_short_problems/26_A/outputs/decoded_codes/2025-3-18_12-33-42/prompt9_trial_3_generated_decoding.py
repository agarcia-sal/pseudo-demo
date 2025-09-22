# Receive Input
t = int(input())

# Initialize Result
semiprime_count = 0

# Iterate Through Numbers
for current_number in range(1, t + 1):
    factor_count = 0
    temp_number = current_number

    # Check for Prime Factors
    for potential_factor in range(2, current_number):
        if temp_number % potential_factor == 0:
            factor_count += 1  # Increment distinct prime factor count
            # While temp_number is divisible by potential_factor
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor  # Remove factor completely

    # Determine Semiprime
    if factor_count == 2:  # Exactly two distinct prime factors
        semiprime_count += 1  # Increment semiprime count

# Output Result
print(semiprime_count)
