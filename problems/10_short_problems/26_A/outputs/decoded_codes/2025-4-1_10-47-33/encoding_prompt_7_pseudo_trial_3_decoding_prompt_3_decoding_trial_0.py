def count_semiprimes(limit):
    semiprime_count = 0

    for i in range(1, limit + 1):
        divisor_count = 0
        current_number = i

        for potential_divisor in range(2, i):
            if current_number % potential_divisor == 0:
                divisor_count += 1
                # Keep dividing current_number by potential_divisor
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor

        # A semiprime has exactly two distinct prime factors
        if divisor_count == 2:
            semiprime_count += 1

    return semiprime_count


# Read input limit from the user
input_limit = int(input())
output = count_semiprimes(input_limit)
print(output)
