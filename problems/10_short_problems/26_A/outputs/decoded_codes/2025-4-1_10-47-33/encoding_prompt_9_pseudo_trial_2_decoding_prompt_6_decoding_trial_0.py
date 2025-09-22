# Get User Input
maximum_number = int(input())  # Read a positive integer from the user

# Initialize count of prime numbers
prime_count = 0  # This will hold the total number of prime numbers found

# Loop through each number from 1 to maximum_number
for current_number in range(1, maximum_number + 1):
    factor_count = 0  # Initialize a count for factors
    remaining_number = current_number  # Set remaining number to current number

    # Check for factors
    for potential_factor in range(2, current_number):  # Check factors from 2 to one less than current_number
        if remaining_number % potential_factor == 0:  # If divisible
            factor_count += 1  # Increase the factor count
            # Remove the factor from remaining_number
            while remaining_number % potential_factor == 0:  
                remaining_number //= potential_factor  # Divide remaining_number by potential_factor

    # Identify if current number is prime
    if factor_count == 1:  # A prime number has exactly two factors: 1 and itself
        prime_count += 1  # Increase the prime count if it's a prime

# Output the result
print(prime_count)  # Display the total number of prime numbers found
