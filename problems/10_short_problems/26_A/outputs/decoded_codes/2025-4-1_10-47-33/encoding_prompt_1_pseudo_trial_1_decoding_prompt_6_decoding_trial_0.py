# Read an integer input representing the upper limit for checking prime numbers
upper_limit = int(input())

# Initialize the variable to count prime numbers
prime_count = 0

# Loop through each number from 1 to upper_limit (inclusive)
for current_number in range(1, upper_limit + 1):
    # Initialize a variable to count divisors
    divisor_count = 0
    
    # Check for divisors from 2 to current_number (exclusive)
    for divisor in range(2, current_number):
        # If current_number is divisible by divisor
        if current_number % divisor == 0:
            # Increment divisor count
            divisor_count += 1
            # Reduce current_number by removing all factors of divisor
            while current_number % divisor == 0:
                current_number //= divisor

    # Check if the number has exactly 2 distinct divisors (1 and itself)
    if divisor_count == 1 and current_number > 1:  # 1 is not a prime number
        prime_count += 1  # Increment prime count if current_number is prime

# Output the total number of prime numbers found
print(prime_count)
