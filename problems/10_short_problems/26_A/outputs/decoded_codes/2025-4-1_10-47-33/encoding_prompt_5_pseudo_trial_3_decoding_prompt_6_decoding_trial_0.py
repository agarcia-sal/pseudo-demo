# Start of the program

# Input - Get a number t from the user
t = int(input())

# Initialize a Counter
semiprime_count = 0  # This will keep track of how many semiprimes are found

# Iterate Through Each Number from 1 to t
for current_number in range(1, t + 1):
    factor_count = 0  # Count of distinct prime factors
    temp_number = current_number  # Temporary variable to factor the current number

    # Find Prime Factors
    for possible_prime in range(2, current_number):
        if temp_number % possible_prime == 0:  # Check if it's divisible
            factor_count += 1  # Found a prime factor
            
            # Reduce Temp Number
            while temp_number % possible_prime == 0:
                temp_number //= possible_prime  # Divide temp_number by possible_prime

    # Check for Semiprime
    if factor_count == 2:  # Check if it has exactly two distinct prime factors
        semiprime_count += 1  # Increment counter for semiprimes

# Output the Result
print(semiprime_count)  # This prints the total number of semiprimes found from 1 to t

# End of the program
