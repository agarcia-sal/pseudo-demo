# Step 1: Receive input from the user
upper_limit = int(input())  # The upper limit (t) is received as an integer

# Step 2: Initialize a counter for semi-primes
semiprime_count = 0  # Variable to keep track of the number of semiprimes

# Step 3: Loop through each number from 1 to upper_limit
for current_number in range(1, upper_limit + 1):
    # Initialize a counter for the number of distinct prime factors
    prime_factor_count = 0  
    divided_number = current_number  # We will divide this by its prime factors

    # Step 4: Identify prime factors for the current number
    for possible_factor in range(2, current_number):  # Check factors from 2 to current_number - 1
        if divided_number % possible_factor == 0:  # If divisible, it's a prime factor
            prime_factor_count += 1  # Increase prime factor count
            
            # Divide divided_number by possible_factor while it's still divisible
            while divided_number % possible_factor == 0:
                divided_number //= possible_factor  # Perform integer division

    # Step 5: Check for the semiprime condition
    if prime_factor_count == 2:  # A semiprime has exactly 2 prime factors
        semiprime_count += 1  # Increment the semiprime count

# Step 6: Output the result
print(semiprime_count)  # Print the total count of semiprime numbers
