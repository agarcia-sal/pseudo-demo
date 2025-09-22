# Start
# Define variable `threshold`
threshold = int(input())  # Get the input value representing the upper limit for counting semiprime numbers.

# Define variable `semiprime_count`
semiprime_count = 0  # Initialize to zero to keep track of the number of semiprime numbers found.

# For each number `current_number` from 1 to `threshold` (inclusive)
for current_number in range(1, threshold + 1):
    # Initialize variable `divisor_count`
    divisor_count = 0  # Set to zero to count unique prime factors of `current_number`.
    
    # Define variable `temp_number`
    temp_number = current_number  # Set to `current_number` for modification in the next steps.
    
    # For each potential_divisor from 2 to `current_number - 1`
    for potential_divisor in range(2, current_number):
        # If `temp_number` is divisible by `potential_divisor`
        if temp_number % potential_divisor == 0:
            # Increment `divisor_count` by 1 (identified a prime factor).
            divisor_count += 1
            
            # While `temp_number` is divisible by `potential_divisor`
            while temp_number % potential_divisor == 0:
                # Divide `temp_number` by `potential_divisor` to remove this factor.
                temp_number //= potential_divisor
                
    # Check if `divisor_count` is exactly 2
    if divisor_count == 2:
        # If it is, increment `semiprime_count` by 1 (this confirms `current_number` is a semiprime).
        semiprime_count += 1 

# Output the value of `semiprime_count`
print(semiprime_count)  # This displays the total number of semiprime numbers found up to `threshold`.
# End
