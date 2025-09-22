# Start by receiving an integer input called total_numbers
total_numbers = int(input())

# Initialize a variable prime_count to zero; this will keep track of how many prime numbers are found
prime_count = 0

# For each integer current_number from 1 to total_numbers (inclusive)
for current_number in range(1, total_numbers + 1):
    # Set a counter divisor_count to zero; this will count how many distinct divisors the current number has
    divisor_count = 0
    # Set a variable numerator to current_number
    numerator = current_number
    
    # For each integer potential_divisor starting from 2 up to (but not including) current_number
    for potential_divisor in range(2, current_number):
        # Check if numerator is divisible by potential_divisor
        if numerator % potential_divisor == 0:
            # If it is, increment divisor_count by 1
            divisor_count += 1
            # While numerator is still divisible by potential_divisor, divide numerator by potential_divisor
            while numerator % potential_divisor == 0:
                numerator //= potential_divisor  # Remove all factors of potential_divisor from numerator
    
    # After finishing the inner loop, check if divisor_count equals 2
    if divisor_count == 0 and current_number > 1:  # 0 divisors means prime, except for number 1 which is not prime
        prime_count += 1  # Increment prime_count by 1 indicating that current_number is a prime number

# After processing all numbers, output the value of prime_count
print(prime_count)
