def count_numbers_with_exactly_two_distinct_prime_factors(limit: int) -> int:
    """
    Counts numbers in the range [2, limit] that have exactly two distinct prime factors.
    
    Args:
        limit (int): The upper bound of the range (inclusive).
        
    Returns:
        int: Count of numbers with exactly two distinct prime factors.
    """
    count = 0
    for number in range(2, limit + 1):
        distinct_factor_count = 0
        temp = number
        divisor = 2

        # Check for prime factors up to sqrt(temp)
        while divisor * divisor <= temp:
            if temp % divisor == 0:
                distinct_factor_count += 1
                while temp % divisor == 0:
                    temp //= divisor
                # If more than 2 distinct factors found, no need to continue
                if distinct_factor_count > 2:
                    break
            divisor += 1

        # If after division temp > 1, then temp itself is prime and counts as one distinct factor
        if temp > 1:
            distinct_factor_count += 1

        if distinct_factor_count == 2:
            count += 1

    return count


if __name__ == "__main__":
    upper_bound = int(input())
    result = count_numbers_with_exactly_two_distinct_prime_factors(upper_bound)
    print(result)
