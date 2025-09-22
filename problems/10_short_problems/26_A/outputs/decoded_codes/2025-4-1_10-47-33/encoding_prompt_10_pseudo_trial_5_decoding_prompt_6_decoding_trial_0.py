# Step 1: Read the number of test cases from user input
test_cases = int(input())

# Step 2: Initialize a variable to store the count of prime numbers
prime_count = 0

# Step 3: Loop through each number from 1 to test_cases
for current_number in range(1, test_cases + 1):
    # Initialize a counter for factors
    factor_count = 0
    # Set variable num to the current number
    num = current_number

    # Step 4: Check for factors of num
    for divisor in range(2, current_number):
        if num % divisor == 0:  # num is divisible by divisor
            factor_count += 1  # Increment factor count
            # While num is divisible by divisor, divide num by divisor
            while num % divisor == 0:
                num //= divisor

    # Step 5: Determine if current_number is a prime number
    if factor_count == 2:  # Only two distinct positive divisors
        prime_count += 1  # Increment the prime number count

# Step 6: Output the total count of prime numbers found
print(prime_count)
