t = int(input())
result = 0

for current_number in range(1, t + 1):
    factor_count = 0
    temp_number = current_number

    for potential_factor in range(2, current_number):
        if temp_number % potential_factor == 0:
            factor_count += 1
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor
    
    if factor_count == 2:
        result += 1

print(result)


def count_numbers_with_exactly_k_prime_factors(t, k):
    result = 0

    for current_number in range(1, t + 1):
        factor_count = 0
        temp_number = current_number

        for potential_factor in range(2, int(temp_number**0.5) + 1):
            if temp_number % potential_factor == 0:
                factor_count += 1
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        if temp_number > 1:  # If there's any prime factor larger than sqrt
            factor_count += 1
        
        if factor_count == k:
            result += 1

    return result

t = int(input())
print(count_numbers_with_exactly_k_prime_factors(t, 2))
