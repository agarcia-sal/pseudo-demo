# 1. Start

# 2. Input
t = int(input())

# 3. Initialize a Counter
semiprime_count = 0

# 4. Iterate Through Each Number
for current_number in range(1, t + 1):
    # Initialize a variable factor_count to 0
    factor_count = 0
    temp_number = current_number

    # 5. Find Prime Factors
    for possible_prime in range(2, current_number):
        if temp_number % possible_prime == 0:
            # Increment factor_count by 1
            factor_count += 1
            
            # Reduce Temp Number
            while temp_number % possible_prime == 0:
                # Divide temp_number by possible_prime
                temp_number //= possible_prime

    # 6. Check for Semiprime
    if factor_count == 2:
        # Increment semiprime_count by 1
        semiprime_count += 1

# 7. Output the Result
print(semiprime_count)

# 8. End
