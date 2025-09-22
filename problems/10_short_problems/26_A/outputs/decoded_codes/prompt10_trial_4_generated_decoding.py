def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_with_two_distinct_prime_factors(t):
    """Count how many numbers from 1 to t have exactly two distinct prime factors."""
    res = 0  # Initialize result

    for i in range(1, t + 1):
        cnt = 0  # Counter for distinct prime factors
        num = i
        
        # Check for prime factors starting from the smallest prime (2)
        for j in range(2, num):
            if num % j == 0 and is_prime(j):
                cnt += 1  # Found a distinct prime factor
                # Remove the prime factor from num
                while num % j == 0:
                    num //= j
            
            # Short-circuit if we've already found 2 distinct prime factors
            if cnt > 2:
                break
        
        # Check if we found exactly 2 distinct prime factors
        if cnt == 2:
            res += 1  # Increment the result counter

    return res

# Input handling
t = int(input())  # Prompt user for input

# Calculate the result and print it
result = count_numbers_with_two_distinct_prime_factors(t)
print(result)
