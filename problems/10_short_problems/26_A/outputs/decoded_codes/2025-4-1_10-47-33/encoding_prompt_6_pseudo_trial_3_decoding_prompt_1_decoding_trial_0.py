# Read an integer input that represents the upper limit for checking prime numbers
t = int(input())

# Initialize a variable to keep track of the count of prime numbers found
prime_count = 0

# Loop through each number from 1 to t (inclusive)
for i in range(1, t + 1):
    
    # Initialize a counter to track the number of unique prime factors for the current number
    unique_prime_factors_count = 0
    
    # Create a variable 'current_number' and set it to the current number 'i'
    current_number = i
    
    # Check for potential prime factors starting from 2 up to current_number - 1
    for j in range(2, current_number):
        
        # If 'j' is a factor of 'current_number'
        if current_number % j == 0:
            # Increment the count of unique prime factors
            unique_prime_factors_count += 1
            
            # Divide 'current_number' by 'j' until it is no longer divisible by 'j'
            while current_number % j == 0:
                current_number //= j

    # After checking all factors, if the count of unique prime factors is exactly 2
    if unique_prime_factors_count == 2:
        # Increment the prime count, as this indicates 'i' is a prime number
        prime_count += 1

# After checking all numbers, output the total count of prime numbers found
print(prime_count)
