def count_semi_primes(input_number):
    result_counter = 0

    for current_number in range(1, input_number + 1):
        divisor_count = 0
        temp_number = current_number

        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:
                divisor_count += 1
                
                # Reduce temp_number by removing all occurrences of the potential_divisor
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
        
        # Check if the number has exactly two distinct prime factors
        if divisor_count == 2:
            result_counter += 1

    return result_counter

# Example usage
t = int(input())
print(count_semi_primes(t))
