# Input the number
total_count = int(input())

# Initialize a result counter
result = 0  # This will keep track of how many numbers have exactly two distinct prime factors

# Loop through each number
for current_number in range(1, total_count + 1):
    distinct_prime_count = 0  # To count the distinct prime factors of current_number
    temp_number = current_number  # Work with its value without losing the original number

    # Find prime factors
    for potential_factor in range(2, current_number):  # Possible factors from 2 up to current_number - 1
        if temp_number % potential_factor == 0:  # Check if it's divisible
            distinct_prime_count += 1  # Increase count for a distinct prime factor
            # Remove that factor completely
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor  # Effectively removing that factor

    # Count numbers with exactly two distinct primes
    if distinct_prime_count == 2:  # Check if count of distinct prime factors is exactly 2
        result += 1  # Increment result by 1

# Output the result
print(result)  # Prints how many numbers had exactly two distinct prime factors
