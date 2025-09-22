def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_distinct_prime_factors(number):
    """Count the distinct prime factors of a given number."""
    cnt = 0
    num = number
    
    for j in range(2, number):
        if num % j == 0 and is_prime(j):
            cnt += 1
            while num % j == 0:
                num //= j
        if cnt > 2:  # Early exit if more than 2 distinct prime factors found
            return cnt
            
    return cnt

def main():
    # Input Number of Test Cases
    t = int(input())
    
    # Initialize Result Counter
    res = 0
    
    # Loop Through Each Number from 1 to t
    for i in range(1, t + 1):
        cnt = count_distinct_prime_factors(i)
        
        # Check for Prime Condition
        if cnt == 2:  # Exactly two distinct prime factors
            res += 1  # Count this number as valid

    # Output Result
    print(res)

# Start Program
if __name__ == "__main__":
    main()
