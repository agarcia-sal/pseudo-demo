def has_exactly_two_distinct_prime_factors(n):
    distinct_prime_count = 0
    current_value = n
    
    for potential_prime in range(2, n):
        if current_value % potential_prime == 0:
            distinct_prime_count += 1
            while current_value % potential_prime == 0:
                current_value //= potential_prime
        if distinct_prime_count > 2:  # Early exit if more than 2 distinct primes
            return False
    return distinct_prime_count == 2

t = int(input())
total_count = 0

for current_number in range(1, t + 1):
    if has_exactly_two_distinct_prime_factors(current_number):
        total_count += 1

print(total_count)
