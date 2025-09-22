def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for potential_factor in range(2, int(number**0.5) + 1):
        if number % potential_factor == 0:
            return False
    return True

def count_distinct_prime_factors(num):
    """Count distinct prime factors of a given number."""
    distinct_prime_count = 0
    temp_number = num
    for potential_factor in range(2, num + 1):
        if temp_number < potential_factor:
            break
        if temp_number % potential_factor == 0 and is_prime(potential_factor):
            distinct_prime_count += 1
            while temp_number % potential_factor == 0:
                temp_number //= potential_factor
    return distinct_prime_count

def count_numbers_with_two_distinct_prime_factors(total_count):
    """Count how many numbers from 1 to total_count have exactly two distinct prime factors."""
    result = 0
    for current_number in range(1, total_count + 1):
        if count_distinct_prime_factors(current_number) == 2:
            result += 1
    return result

def main():
    total_count = int(input())  # Read the integer input
    result = count_numbers_with_two_distinct_prime_factors(total_count)
    print(result)  # Output the result

if __name__ == "__main__":
    main()
