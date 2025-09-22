def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semi_primes(t):
    """Count the number of semi-prime numbers up to a given integer t."""
    total_semi_primes = 0
    
    for current_number in range(1, t + 1):
        divisor_count = 0
        temp_number = current_number
        
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:
                divisor_count += 1
                
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
        
        if divisor_count == 2:
            total_semi_primes += 1
            
    return total_semi_primes

# Accept input from the user
t = int(input())
# Call the function and print the result
result = count_semi_primes(t)
print(result)
