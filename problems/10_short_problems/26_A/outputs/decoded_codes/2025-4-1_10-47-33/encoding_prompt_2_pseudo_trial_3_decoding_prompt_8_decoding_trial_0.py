def count_numbers_with_two_distinct_prime_factors():
    total_count = int(input())
    result = 0

    for current_number in range(1, total_count + 1):
        distinct_prime_count = 0
        temp_number = current_number

        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:
                distinct_prime_count += 1
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        if distinct_prime_count == 2:
            result += 1

    print(result)

count_numbers_with_two_distinct_prime_factors()
