# Start of the program

# Step 2: Define the Input
total_numbers = int(input())  # Read an integer value that represents the upper limit of the range

# Step 3: Initialize Count
prime_count = 0  # This will keep track of the number of prime numbers found

# Step 4: Iterate Over Each Number
for current_number in range(1, total_numbers + 1):  # Loop from 1 to total_numbers inclusive
    divisor_count = 0  # Count of divisors for the current number
    temp_number = current_number  # Temporary variable to check divisibility

    # Step 5: Check for Divisibility
    for potential_divisor in range(2, current_number):  # Loop through potential divisors
        if temp_number % potential_divisor == 0:  # Check if divisible
            divisor_count += 1  # Found a divisor
            # While divisible, keep dividing temp_number
            while temp_number % potential_divisor == 0:
                temp_number //= potential_divisor  # Divide temp_number by the potential divisor

    # Step 6: Determine If Prime
    if divisor_count == 1:  # A number is prime if it has exactly one divisor (itself) in this context
        prime_count += 1  # Count this current number as prime

# Step 7: Output the Result
print(prime_count)  # Print the total number of prime numbers
