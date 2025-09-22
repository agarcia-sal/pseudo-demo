def count_semi_primes(t):
    """
    Count the number of semi-prime numbers in the range from 1 to t.
    
    A semi-prime is defined as a natural number that is the product of two 
    distinct prime numbers.
    
    Args:
        t (int): The upper limit of the range to check for semi-primes.
    
    Returns:
        int: The count of semi-prime numbers between 1 and t.
    """
    total_semi_primes = 0

    for i in range(1, t + 1):
        divisor_count = 0
        current_number = i
        
        # Check for prime factors from 2 to i-1
        for j in range(2, current_number):
            if current_number % j == 0:  # j is a divisor
                divisor_count += 1
                
                # Divide out all powers of j from current_number
                while current_number % j == 0:
                    current_number //= j
            
            # If we already found two distinct prime factors, we can stop checking further
            if divisor_count > 2:
                break
        
        # Check if we found exactly two distinct prime factors
        if divisor_count == 2:
            total_semi_primes += 1

    return total_semi_primes

# Input and Output application (example only)
t = int(input())
print(count_semi_primes(t))
