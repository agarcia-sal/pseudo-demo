# Start Program

# Get the input: Read an integer value from the user which represents the upper limit
total = int(input())  # Since the input is expected to be an integer

# Initialize count of prime numbers
prime_count = 0  # This will keep track of how many prime numbers are found

# Iterate through possible numbers
for current_number in range(1, total + 1):
    divisor_count = 0  # Count of divisors for current_number
    working_num = current_number  # Number to check for divisibility
    
    # Check for divisibility
    for potential_divisor in range(2, current_number):  # Check divisibility from 2 to current_number - 1
        if working_num % potential_divisor == 0:  # If divisible
            divisor_count += 1  # Increment count of divisors
            while working_num % potential_divisor == 0:  # Divide working_num by potential_divisor until it no longer divides evenly
                working_num //= potential_divisor  # Perform integer division
    
    # Determine if prime
    if divisor_count == 2:  # If exactly two divisors, it's prime
        prime_count += 1  # Increment the count of prime numbers

# Output result
print(prime_count)  # Print the total number of prime numbers found

# End Program
