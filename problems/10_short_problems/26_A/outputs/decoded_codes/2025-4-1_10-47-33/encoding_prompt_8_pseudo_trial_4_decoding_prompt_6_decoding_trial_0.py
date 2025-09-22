# Start Program

# Get Input: Read an integer value from the user
total_numbers = int(input())  # Variable to store the upper limit

# Initialize Count: Variable to keep track of how many numbers meet the criteria
result = 0

# Iterate Through Numbers: Loop from 1 to total_numbers
for current_number in range(1, total_numbers + 1):
    # Initialize prime factor count for the current number
    prime_factor_count = 0
    # Create a temporary number to work with
    temp_number = current_number

    # Check for Prime Factors: Loop to find factors from 2 to current_number - 1
    for potential_factor in range(2, current_number):
        # Check if temp_number is divisible by potential_factor
        if temp_number % potential_factor == 0:
            # Increment count of unique prime factors found
            prime_factor_count += 1
            # Divide out all occurrences of this factor
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor

    # Evaluate Condition: Check if we found exactly two distinct prime factors
    if prime_factor_count == 2:
        result += 1  # Found a number that is the product of exactly two primes

# Output the Result: Print the total count of such numbers
print(result)

# End Program
