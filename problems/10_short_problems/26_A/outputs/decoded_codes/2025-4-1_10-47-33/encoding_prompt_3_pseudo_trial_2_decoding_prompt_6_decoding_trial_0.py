# Get the number of test cases from user input
test_case_count = int(input())

# Initialize a result variable to store count of prime numbers
prime_count = 0

# Loop over each number from 1 to the value of test_case_count
for current_number in range(1, test_case_count + 1):
    # Initialize a counter to track factors
    factor_count = 0
    
    # Set temp_number to current number for factorization
    temp_number = current_number
    
    # Loop over possible factors from 2 to current_number - 1
    for potential_factor in range(2, current_number):
        # Check if potential_factor divides temp_number
        if temp_number % potential_factor == 0:
            # If it is a factor, increment the counter
            factor_count += 1
            
            # Continuously divide temp_number by potential_factor
            while temp_number % potential_factor == 0:
                temp_number = temp_number // potential_factor
                
    # If exactly two distinct factors were found, it is a prime number
    if factor_count == 1 and current_number > 1:  # Adjust for prime definition (1 is not prime)
        prime_count += 1

# Output the count of prime numbers found
print(prime_count)
