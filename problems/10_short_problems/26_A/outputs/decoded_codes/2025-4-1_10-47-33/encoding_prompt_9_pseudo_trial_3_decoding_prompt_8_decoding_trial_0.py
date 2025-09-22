def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    semiprime_count = 0

    for current_number in range(1, t + 1):
        distinct_prime_count = 0
        number = current_number
        for potential_factor in range(2, current_number):
            if number % potential_factor == 0 and is_prime(potential_factor):
                distinct_prime_count += 1
                while number % potential_factor == 0:
                    number //= potential_factor

        if distinct_prime_count == 2:
            semiprime_count += 1
            
    return semiprime_count

t = int(input())
print(count_semiprimes(t))
