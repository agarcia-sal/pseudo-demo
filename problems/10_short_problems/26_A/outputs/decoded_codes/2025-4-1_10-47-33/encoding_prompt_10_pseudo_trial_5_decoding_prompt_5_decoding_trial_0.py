# Function to count prime numbers up to a given number
def count_prime_numbers():
    # Read the number of test cases
    t = int(input())
    
    # Initialize the count of prime numbers
    prime_count = 0
    
    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize a counter for the number of factors
        factor_count = 0
        num = i
        
        # Check for factors of num
        for j in range(2, i):
            # If num is divisible by j, it means j is a factor
            if num % j == 0:
                # Increment the factor counter
                factor_count += 1
                
                # While num is divisible by j, divide it by j
                while num % j == 0:
                    num //= j
        
        # Check if the current number i is a prime
        if factor_count == 1:  # Since we're counting the factor of 1 (number itself)
            prime_count += 1
    
    # Output the total count of prime numbers found
    print(prime_count)

# Call the function to execute
count_prime_numbers()
