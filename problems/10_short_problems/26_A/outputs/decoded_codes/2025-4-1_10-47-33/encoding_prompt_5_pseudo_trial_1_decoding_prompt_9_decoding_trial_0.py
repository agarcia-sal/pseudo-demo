# Function to check if a number is semiprime
def is_semiprime(num):
    prime_factor_count = 0  # Counter for counting distinct prime factors
    original_number = num     # Store the original number for processing

    # Loop through all numbers starting from 2 up to the current number
    for potential_factor in range(2, original_number):
        if num % potential_factor == 0:  # Check for divisibility
            prime_factor_count += 1  # Found a new prime factor
            
            # Continuously divide the number by this factor
            while num % potential_factor == 0:
                num //= potential_factor

    return prime_factor_count == 2  # Return True if exactly two distinct prime factors

# Main Code
upper_limit = int(input())  # Take input from user for the upper limit
semiprime_count = 0  # Initialize semiprime counter

# Loop through each number from 1 to upper limit
for number in range(1, upper_limit + 1):
    if is_semiprime(number):  # Check if the number is semiprime
        semiprime_count += 1  # Increment count if it is semiprime

# Output the total count of semiprime numbers found
print(semiprime_count)
