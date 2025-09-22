# Start Program

# Step 2: Receive Input
limit = int(input())  # Prompt the user to enter a positive integer limit

# Step 3: Initialize Count
count_of_products = 0  # This will hold the total number of valid products found

# Step 4: Iterate Through Numbers
for current_number in range(1, limit + 1):
    distinct_prime_factors = 0  # Track distinct prime factors for the current number
    temporary_number = current_number  # Work with a temporary copy of the current number

    # Step 5: Check for Prime Factors
    for potential_prime in range(2, current_number):
        if temporary_number % potential_prime == 0:  # Check if potential_prime is a factor
            distinct_prime_factors += 1  # Found a distinct prime factor
            # Remove that factor from temporary_number
            while temporary_number % potential_prime == 0:
                temporary_number //= potential_prime

    # Step 6: Check the Condition
    if distinct_prime_factors == 2:  # If we found exactly 2 distinct prime factors
        count_of_products += 1  # Increment the count

# Step 7: Output Result
print(count_of_products)  # Print the count of products of exactly two distinct prime numbers

# End Program
