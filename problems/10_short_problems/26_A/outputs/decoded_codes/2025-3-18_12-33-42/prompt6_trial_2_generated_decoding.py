# Input: A positive integer t
total_numbers = int(input())  # Reads the positive integer input

# Initialize a variable to count special numbers
special_number_count = 0

# Loop through each integer from 1 to total_numbers
for current_number in range(1, total_numbers + 1):
    # Initialize a counter for prime factors
    prime_factor_count = 0
    # Store the current number to check its factors
    number_to_check = current_number

    # Loop through possible divisors from 2 to current_number - 1
    for divisor in range(2, current_number):
        # Check if divisor is a factor of number_to_check
        if number_to_check % divisor == 0:
            # Found a prime factor; increment the counter
            prime_factor_count += 1
            # Remove all occurrences of the divisor from number_to_check
            while number_to_check % divisor == 0:
                number_to_check //= divisor

    # Check if the number has exactly two distinct prime factors
    if prime_factor_count == 2:
        # Count this number as a special number
        special_number_count += 1

# Output: The count of numbers with exactly two distinct prime factors
print(special_number_count)
