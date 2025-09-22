def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_distinct_prime_factors(num):
    cnt = 0
    for j in range(2, num):
        if num % j == 0 and is_prime(j):
            cnt += 1
            while num % j == 0:
                num //= j
    return cnt

def main():
    # Input Number of Test Cases
    t = int(input())
    
    # Initialize Result Counter
    res = 0
    
    # Loop Through Each Number from 1 to t
    for i in range(1, t + 1):
        # Get the count of distinct prime factors
        cnt = count_distinct_prime_factors(i)
        
        # Check for Prime Condition
        if cnt == 2:
            res += 1
    
    # Output Result
    print(res)

# Start the program
main()
