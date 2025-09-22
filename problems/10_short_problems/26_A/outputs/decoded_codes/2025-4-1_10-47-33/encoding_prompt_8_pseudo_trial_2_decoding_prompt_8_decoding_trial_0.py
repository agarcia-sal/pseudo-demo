def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semiprimes(limit):
    semiprime_count = 0

    for current_number in range(1, limit + 1):
        prime_factor_count = 0
        temp_number = current_number

        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:
                prime_factor_count += 1
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        if prime_factor_count == 2:
            semiprime_count += 1
    
    return semiprime_count

# Main execution
limit = int(input())
result = count_semiprimes(limit)
print(result)
