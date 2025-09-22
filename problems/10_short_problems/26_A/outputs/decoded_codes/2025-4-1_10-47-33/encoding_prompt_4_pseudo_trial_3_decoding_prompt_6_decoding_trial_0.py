# Begin the program

# Read the input value indicating how many numbers to check
total_numbers = int(input())  # Read integer input for total numbers

# Initialize a counter for numbers with exactly two prime factors
prime_factor_count = 0

# Loop through each number from 1 to total_numbers
for number in range(1, total_numbers + 1):  # Ranges from 1 to total_numbers (inclusive)
    
    # Initialize a count for prime factors found in the current number
    factor_count = 0
    current_number = number
    
    # Check for factors from 2 up to the current number
    for factor in range(2, current_number + 1):  # Check factors from 2 to current_number (inclusive)
        
        # If the factor divides the current number
        if current_number % factor == 0:  # Check modulus
            # Increment the count of found prime factors
            factor_count += 1
            
            # Divide the current number by the factor until it no longer divides evenly
            while current_number % factor == 0:  # Continue while it divides evenly
                current_number //= factor  # Use floor division to update current_number
            
        # End of the if statement
        
    # End of the for loop for factors
    
    # If exactly two distinct prime factors were found
    if factor_count == 2:  # Check if the count of distinct prime factors is exactly 2
        # Increment the total count of such numbers
        prime_factor_count += 1  # Increment the count of numbers meeting the condition
        
# End of the for loop for numbers

# Output the total count of numbers with exactly two distinct prime factors
print(prime_factor_count)  # Print the result

# End the program
