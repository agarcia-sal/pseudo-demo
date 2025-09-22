# Function to count semi-prime numbers up to a given number t
def count_semi_primes(t):
    # Initialize the total count of semi-prime numbers to 0
    total_semi_primes = 0
    
    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize the count of distinct prime factors for the current number
        divisor_count = 0
        current_number = i
        
        # Check for possible divisors from 2 to (i-1)
        for j in range(2, i):
            if current_number % j == 0:  # If j is a divisor of current_number
                divisor_count += 1  # Count this as a distinct prime factor
                
                # Divide current_number by j until it's no longer divisible
                while current_number % j == 0:
                    current_number //= j
        
        # If there are exactly 2 distinct prime factors, count it as a semi-prime
        if divisor_count == 2:
            total_semi_primes += 1  # Increment the semi-prime count
    
    # Return the total count of semi-prime numbers found
    return total_semi_primes

# Input: an integer t to determine the range limit for semi-primes
t = int(input())  # Read input from the user

# Output: Print the count of semi-prime numbers up to t
print(count_semi_primes(t))  # Display the result
