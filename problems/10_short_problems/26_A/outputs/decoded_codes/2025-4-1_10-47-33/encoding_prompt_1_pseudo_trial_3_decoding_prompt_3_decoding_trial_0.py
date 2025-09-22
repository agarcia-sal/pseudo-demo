def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semi_primes(t):
    """Count the number of semi-prime numbers up to a given number t."""
    result = 0  # Initialize result count of semi-prime numbers
    
    # Iterate through each number from 1 to t
    for i in range(1, t + 1):
        count_divisors = 0  # Count distinct prime factors
        current_number = i  # Number to factor
        
        # Check for prime factors from 2 up to i-1
        for j in range(2, i):
            if current_number % j == 0 and is_prime(j):
                count_divisors += 1  # Found a new prime factor
                # Factor out j completely from current_number
                while current_number % j == 0:
                    current_number //= j
        
        # Check if the number of distinct prime factors is exactly 2
        if count_divisors == 2:
            result += 1  # i is a semi-prime number
            
    print(result)  # Output the total count of semi-prime numbers

# Input: Read an integer value t
t = int(input())

# Call the function with user-input
count_semi_primes(t)
