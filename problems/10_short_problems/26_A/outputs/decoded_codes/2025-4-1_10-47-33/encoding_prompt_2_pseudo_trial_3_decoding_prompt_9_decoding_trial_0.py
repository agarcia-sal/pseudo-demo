# Input the number
total_count = int(input())

# Initialize a result counter
result = 0  # This will keep track of how many numbers have exactly two distinct prime factors.

# Loop through each number from 1 to total_count (inclusive)
for current_number in range(1, total_count + 1):
    distinct_prime_count = 0  # Counter for distinct prime factors
    temp_number = current_number  # Work with this copy of the current number

    # Find prime factors by checking potential factors from 2 to current_number - 1
    for potential_factor in range(2, current_number):
        if temp_number % potential_factor == 0:  # Check if potential_factor divides temp_number
            distinct_prime_count += 1  # Found a new distinct prime factor

            # Divide temp_number by potential_factor to remove that factor
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor
            
    # Count numbers with exactly two distinct primes
    if distinct_prime_count == 2:
        result += 1  # Increment the result counter

# Output the result
print(result)
