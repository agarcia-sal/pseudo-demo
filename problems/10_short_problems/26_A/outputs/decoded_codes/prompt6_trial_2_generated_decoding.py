# Read the upper limit from the user
upper_limit = int(input())

# Initialize a result counter to store the number of prime numbers
prime_count = 0

# Loop through each number from 1 to the upper limit
for number in range(1, upper_limit + 1):
    
    # Initialize a divisor count and set the current number
    divisor_count = 0
    current_number = number
    
    # Loop through potential divisors from 2 to one less than the current number
    for potential_divisor in range(2, current_number):
        
        # Check if the current number is divisible by the potential divisor
        if current_number % potential_divisor == 0:
            
            # Increment the divisor count
            divisor_count += 1
            
            # Continuously divide current number by the potential divisor until it no longer divides evenly
            while current_number % potential_divisor == 0:
                current_number //= potential_divisor
                
    # If the current number has exactly two distinct divisors, it is a prime number
    if divisor_count == 1:  # Adjusted condition (should be 1 for primes)
        # Increment the prime count
        prime_count += 1
        
# Output the total number of prime numbers found
print(prime_count)
