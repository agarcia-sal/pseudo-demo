# Read an integer value as the upper limit
limit = int(input())

# Initialize semiprime count to 0
semiprime_count = 0

# Loop through numbers from 1 to the limit (inclusive)
for current_number in range(1, limit + 1):
    # Initialize count of distinct prime factors
    prime_factor_count = 0
    number_to_check = current_number
    
    # Find prime factors
    for potential_prime in range(2, current_number):  # Check from 2 to current_number - 1
        if number_to_check % potential_prime == 0:  # If potential prime is a factor
            prime_factor_count += 1  # Increment the count of prime factors
            while number_to_check % potential_prime == 0:  # While it divides evenly
                number_to_check //= potential_prime  # Reduce number_to_check

    # Check if the current number is a semiprime
    if prime_factor_count == 2:
        semiprime_count += 1  # Increment semiprime count

# Output the total count of semiprime numbers
print(semiprime_count)
