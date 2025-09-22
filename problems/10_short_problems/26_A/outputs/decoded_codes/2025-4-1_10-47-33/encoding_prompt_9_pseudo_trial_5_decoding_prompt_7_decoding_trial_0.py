# Function to determine if a number is semiprime
def is_semiprime(n):
    # Initialize counter for distinct prime factors
    prime_factor_count = 0
    divided_number = n

    # Check for prime factors starting from 2
    for possible_factor in range(2, n):
        if divided_number % possible_factor == 0:  # If divisible
            prime_factor_count += 1  # Increment prime factor count
            # Divide out all occurrences of this factor
            while divided_number % possible_factor == 0:
                divided_number //= possible_factor
        # If we found more than 2 unique prime factors, return False early
        if prime_factor_count > 2:
            return False
    
    # A semiprime must have exactly 2 prime factors
    return prime_factor_count == 2

# Main execution flow
t = int(input())  # Get upper limit from user
semiprime_count = 0  # Initialize the counter for semiprimes

# Loop through each number from 1 to t
for current_number in range(1, t + 1):
    # Check if the current number is semiprime
    if is_semiprime(current_number):
        semiprime_count += 1  # Increment the semiprime count

# Output the total count of semiprime numbers
print(semiprime_count)
