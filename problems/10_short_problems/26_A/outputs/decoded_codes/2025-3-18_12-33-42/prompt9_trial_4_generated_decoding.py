# Start by getting the upper limit for counting semiprimes
t = int(input())

# Initialize a counter for the number of semiprime numbers found
semiprime_count = 0

# Loop through each number from 1 to t
for current_number in range(1, t + 1):
    # Count of unique prime factors for the current number
    prime_factor_count = 0
    # Temporary variable for factorization
    temp_number = current_number
    
    # Loop through potential factors from 2 up to one less than current_number
    for factor in range(2, current_number):
        # Check if factor is a divisor of temp_number
        if temp_number % factor == 0:
            # If it is a divisor, count it as a prime factor
            prime_factor_count += 1
            # Divide temp_number by factor as long as it is divisible
            while temp_number % factor == 0:
                temp_number //= factor
    
    # Check if the current number is semiprime
    if prime_factor_count == 2:
        semiprime_count += 1

# Output the total number of semiprime numbers found
print(semiprime_count)
