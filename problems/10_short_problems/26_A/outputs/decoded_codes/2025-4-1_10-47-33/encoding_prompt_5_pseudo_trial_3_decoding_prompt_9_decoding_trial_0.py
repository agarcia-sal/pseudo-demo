# Start the semiprime counting program
t = int(input())  # Get the number `t` from the user

semiprime_count = 0  # Initialize a counter for semiprimes

# Iterate through each number from 1 to t
for current_number in range(1, t + 1):
    factor_count = 0  # Count of distinct prime factors for the current number
    temp_number = current_number  # A temporary variable to factor the number

    # Find prime factors of current_number
    for possible_prime in range(2, current_number):  # Check for factors up to current_number - 1
        if temp_number % possible_prime == 0:  # Check if possible_prime is a factor
            factor_count += 1  # Found a new prime factor
            
            # Reduce temp_number by dividing out possible_prime completely
            while temp_number % possible_prime == 0:
                temp_number //= possible_prime

    # Check if we have exactly 2 distinct prime factors
    if factor_count == 2:
        semiprime_count += 1  # Count this number as a semiprime

# Output the total count of semiprimes found
print(semiprime_count)
