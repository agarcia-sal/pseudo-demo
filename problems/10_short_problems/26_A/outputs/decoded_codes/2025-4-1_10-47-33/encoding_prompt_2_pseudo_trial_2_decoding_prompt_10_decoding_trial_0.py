def count_numbers_with_two_distinct_prime_factors(upper_limit):
    """
    Counts how many numbers from 1 to upper_limit have exactly two distinct prime factors.

    Parameters:
    upper_limit (int): The upper limit to check for numbers.

    Returns:
    int: The count of numbers with exactly two distinct prime factors.
    """
    result = 0

    for number in range(1, upper_limit + 1):
        count = 0
        temp_number = number
        
        # Check for prime factors starting from 2 up to the number itself
        for potential_prime in range(2, number):
            if temp_number % potential_prime == 0:  # Found a prime factor
                count += 1
                
                # Remove this factor completely
                while temp_number % potential_prime == 0:
                    temp_number //= potential_prime
            
            # If we already found 2 distinct prime factors, we can exit early
            if count > 2:
                break
        
        # Only consider numbers with exactly two distinct prime factors
        if count == 2:
            result += 1

    return result

if __name__ == "__main__":
    upper_limit = int(input())
    print(count_numbers_with_two_distinct_prime_factors(upper_limit))
