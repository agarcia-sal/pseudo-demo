# Start

# Input
t = int(input())  # Get a number t from the user

# Initialize a Counter
semiprime_count = 0  # This will track how many semiprimes are found

# Iterate Through Each Number
for current_number in range(1, t + 1):
    factor_count = 0  # Count of distinct prime factors of current_number
    temp_number = current_number  # Initialize temp_number with current_number

    # Find Prime Factors
    for possible_prime in range(2, current_number):
        if temp_number % possible_prime == 0:  # If temp_number is divisible by possible_prime
            factor_count += 1  # Increment the number of distinct prime factors
            
            # Reduce Temp Number
            while temp_number % possible_prime == 0:  # While temp_number is divisible by possible_prime
                temp_number //= possible_prime  # Divide temp_number by possible_prime

    # Check for Semiprime
    if factor_count == 2:  # Check if current_number has exactly two prime factors
        semiprime_count += 1  # Increment the semiprime count

# Output the Result
print(semiprime_count)  # Print the total number of semiprimes from 1 to t

# End
