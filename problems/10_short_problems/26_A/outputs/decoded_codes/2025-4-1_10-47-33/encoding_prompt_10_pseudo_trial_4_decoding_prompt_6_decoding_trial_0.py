# Start Program

# Input Number of Test Cases
test_cases = int(input())  # Reading number of test cases as an integer

# Initialize Result Counter
result_count = 0  # This will hold the count of numbers with exactly two distinct prime factors

# Loop Through Each Number from 1 to test_cases
for current_number in range(1, test_cases + 1):  # Looping from 1 to t
    distinct_prime_factors_count = 0  # This will count the number of distinct prime factors
    num = current_number  # To factorize the current number
    
    # Loop to Find Factors
    for potential_factor in range(2, current_number):  # Checking factors from 2 to current_number-1
        if num % potential_factor == 0:  # If potential_factor is a factor of num
            distinct_prime_factors_count += 1  # Found a new prime factor
            while num % potential_factor == 0:  # While num is divisible by potential_factor
                num //= potential_factor  # Remove the factor potential_factor from num

    # Check for Prime Condition
    if distinct_prime_factors_count == 2:  # Check if there are exactly two distinct prime factors
        result_count += 1  # Count this number as valid

# Output Result
print(result_count)  # Print the total count of numbers with exactly two distinct prime factors

# End Program
