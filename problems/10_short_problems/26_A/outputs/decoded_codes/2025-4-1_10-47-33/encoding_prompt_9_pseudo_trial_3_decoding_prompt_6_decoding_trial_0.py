# Start the program and read an integer 't' from the user.
t = int(input())  # Input upper limit

# Initialize a count variable named 'semiprime_count' to 0.
semiprime_count = 0  # This will track the number of semiprime numbers found

# Loop through each number 'current_number' from 1 to 't' (inclusive).
for current_number in range(1, t + 1):
    # Set a counter named 'distinct_prime_count' to 0.
    distinct_prime_count = 0
    # Set a variable 'number' equal to 'current_number' for factorization.
    number = current_number

    # Loop through each potential factor 'potential_factor' from 2 to 'current_number - 1'.
    for potential_factor in range(2, current_number):
        # Check if 'current_number' is divisible by 'potential_factor'.
        if number % potential_factor == 0:
            # If true, increase 'distinct_prime_count' by 1.
            distinct_prime_count += 1
            
            # While 'number' is divisible by 'potential_factor'.
            while number % potential_factor == 0:
                # Divide 'number' by 'potential_factor'.
                number //= potential_factor

    # After checking all potential factors, if 'distinct_prime_count' is equal to 2.
    if distinct_prime_count == 2:
        # Increase 'semiprime_count' by 1.
        semiprime_count += 1

# Once all numbers have been checked, output the value of 'semiprime_count'.
print(semiprime_count)
