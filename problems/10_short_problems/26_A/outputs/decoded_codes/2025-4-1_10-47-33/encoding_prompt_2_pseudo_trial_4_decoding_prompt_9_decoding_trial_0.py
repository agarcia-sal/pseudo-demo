# Read upper limit for checking numbers
t = int(input())

# Initialize a variable to hold the count of numbers with exactly two distinct prime factors
result = 0

# Loop through all integers from 1 to t (inclusive)
for current_number in range(1, t + 1):
    # Initialize count of distinct prime factors for the current number
    factor_count = 0
    temp_number = current_number  # Temporary variable to manipulate without losing current_number

    # Check for potential prime factors from 2 to current_number - 1
    for potential_factor in range(2, current_number):
        # If temp_number is divisible by potential_factor, then it is a factor
        if temp_number % potential_factor == 0:
            factor_count += 1  # Found a new distinct prime factor
            # Remove all occurrences of the potential_factor
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor

    # After checking all potential factors, check if we found exactly two distinct prime factors
    if factor_count == 2:
        result += 1  # Increment the result count

# Output the total count of numbers with exactly two distinct prime factors
print(result)
