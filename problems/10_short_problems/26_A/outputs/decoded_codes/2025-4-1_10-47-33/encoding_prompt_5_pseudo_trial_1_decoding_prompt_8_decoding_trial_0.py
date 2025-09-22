def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(upper_limit):
    semiprime_count = 0
    
    for current_number in range(1, upper_limit + 1):
        prime_factor_count = 0
        num = current_number
        
        for potential_factor in range(2, num):
            if num % potential_factor == 0 and is_prime(potential_factor):
                prime_factor_count += 1
                while num % potential_factor == 0:
                    num //= potential_factor
            if prime_factor_count > 2:
                break

        if prime_factor_count == 2:
            semiprime_count += 1

    return semiprime_count

upper_limit = int(input())
result = count_semiprimes(upper_limit)
print(result)
