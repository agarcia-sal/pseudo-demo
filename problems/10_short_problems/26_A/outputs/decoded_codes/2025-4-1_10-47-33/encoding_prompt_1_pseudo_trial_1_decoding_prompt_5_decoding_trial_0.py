# Function to count the number of prime numbers up to a given integer
def count_primes():
    # Read input for the upper limit to check for prime numbers
    upper_limit = int(input())
    
    # Initialize the prime count to 0
    prime_count = 0
    
    # Loop through each number from 1 to upper_limit (inclusive)
    for i in range(1, upper_limit + 1):
        # Initialize divisor count for the current number
        divisor_count = 0
        current_number = i
        
        # Check for divisors starting from 2 up to but not including the current number
        for j in range(2, i):
            # If current_number is divisible by j
            if current_number % j == 0:
                divisor_count += 1
                # Reduce current_number by dividing by j until it is no longer divisible
                while current_number % j == 0:
                    current_number //= j
        
        # Determine if current number is prime
        # A prime number has exactly 2 distinct divisors: 1 and itself
        if divisor_count == 2:
            prime_count += 1
    
    # Output the total number of prime numbers found
    print(prime_count)

# Test the function
# Example calls can be added here, such as:
# count_primes() assuming the input is provided through standard input
