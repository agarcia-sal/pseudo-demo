# Read an integer input representing an upper limit
upper_limit = int(input())

# Initialize a counter for special numbers
special_number_count = 0

# Loop through each number from 1 to the upper limit
for current_number in range(1, upper_limit + 1):
    
    # Initialize a counter for unique prime factors
    unique_prime_factor_count = 0
    temp_number = current_number
    
    # Loop through potential factors starting from 2 up to current_number-1
    for factor in range(2, current_number):
        
        # Check if factor is a divisor of temp_number
        if temp_number % factor == 0:
            # Increment the unique prime factor count
            unique_prime_factor_count += 1
            
            # Divide temp_number by factor until it is no longer divisible by factor
            while temp_number % factor == 0:
                temp_number //= factor

    # Check if exactly two unique prime factors were found
    if unique_prime_factor_count == 2:
        # Increment the count of special numbers
        special_number_count += 1

# Output the total count of special numbers
print(special_number_count)
