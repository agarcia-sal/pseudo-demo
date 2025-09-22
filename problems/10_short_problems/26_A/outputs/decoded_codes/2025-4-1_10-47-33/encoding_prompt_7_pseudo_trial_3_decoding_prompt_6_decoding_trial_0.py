def count_semiprimes(limit):
    # Initialize a counter for semiprime numbers
    semiprime_count = 0
    
    # Loop through each number from 1 to the given limit
    for i in range(1, limit + 1):
        # Initialize a counter for the number of divisors
        divisor_count = 0
        current_number = i
        
        # Check for potential divisors from 2 to (i - 1)
        for potential_divisor in range(2, i):
            if current_number % potential_divisor == 0:
                # Increment the divisor count if it divides the current number
                divisor_count += 1
                
                # Divide current number by the potential divisor as long as it is divisible
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor
        
        # If we found exactly 2 distinct prime factors, count it as a semiprime
        if divisor_count == 2:
            semiprime_count += 1
    
    # Return the total count of semiprimes found
    return semiprime_count

# Read an integer value from the user
input_limit = int(input())

# Call the function to count semiprimes and store the result
output = count_semiprimes(input_limit)

# Print the result
print(output)
