# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Start Program

# Receive Input
limit = int(input())

# Initialize Count
count_of_products = 0  # Count of valid products found

# Iterate Through Numbers
for current_number in range(1, limit + 1):
    distinct_prime_factors = 0  # Track distinct prime factors for the current number
    temporary_number = current_number

    # Check for Prime Factors
    for potential_prime in range(2, current_number):
        if temporary_number % potential_prime == 0 and is_prime(potential_prime):
            distinct_prime_factors += 1  # Found a distinct prime factor
            # Remove all occurrences of the potential prime factor
            while temporary_number % potential_prime == 0:
                temporary_number //= potential_prime
        
    # Check the Condition
    if distinct_prime_factors == 2:  # Exactly two distinct prime factors
        count_of_products += 1  # Increment count

# Output Result
print(count_of_products)  # Output the count of products found

# End Program
