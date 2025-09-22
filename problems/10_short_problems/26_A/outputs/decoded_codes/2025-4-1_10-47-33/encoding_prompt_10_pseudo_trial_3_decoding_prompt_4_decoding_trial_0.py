def is_prime(num):
    if num < 2:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

def count_prime_numbers(t):
    # Initialize the count of prime numbers
    prime_count = 0
    # Loop through numbers from 1 to t (inclusive)
    for i in range(1, t + 1):
        if is_prime(i):
            prime_count += 1  # Increase the count if `i` is prime
    return prime_count

# Main program
t = int(input())
result = count_prime_numbers(t)
print(result)
