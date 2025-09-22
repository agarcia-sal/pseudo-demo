def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count how many semiprimes exist from 1 to t."""
    semiprime_count = 0

    # Loop through each number from 1 to t
    for current_number in range(1, t + 1):
        prime_factor_count = 0
        divided_number = current_number

        # Identify prime factors for the current number
        for possible_factor in range(2, divided_number):
            if divided_number % possible_factor == 0 and is_prime(possible_factor):
                prime_factor_count += 1
                # Divide divided_number by possible_factor until it is not divisible
                while divided_number % possible_factor == 0:
                    divided_number //= possible_factor
        
        # Check for semiprime condition
        if prime_factor_count == 2:
            semiprime_count += 1

    return semiprime_count

# Receive input from the user
t = int(input())
result = count_semiprimes(t)

# Output the result
print(result)
