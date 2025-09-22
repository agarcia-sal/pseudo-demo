def is_prime(num):
    # Check if a number is prime
    if num <= 1:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

def count_primes(t):
    # Initialize the count of prime numbers
    prime_count = 0
    
    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Check if the current number is prime
        if is_prime(i):
            prime_count += 1

    return prime_count

def main():
    # Read the number of test cases
    t = int(input())
    
    # Get the total count of prime numbers up to t
    result = count_primes(t)
    
    # Output the total count of prime numbers found
    print(result)

if __name__ == "__main__":
    main()
