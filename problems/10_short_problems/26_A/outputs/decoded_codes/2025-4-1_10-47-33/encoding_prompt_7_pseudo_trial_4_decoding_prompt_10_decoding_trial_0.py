def count_semi_prime_numbers(input_number):
    """
    Counts the number of semi-prime numbers up to the given input number.
    
    A semi-prime number is defined as the product of exactly two prime numbers.
    
    Args:
        input_number (int): The upper limit to count semi-prime numbers.
        
    Returns:
        int: The count of semi-prime numbers up to input_number.
    """
    result = 0

    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Get all prime numbers up to input_number
    primes = [num for num in range(2, input_number + 1) if is_prime(num)]

    # Check for semi-prime numbers
    semi_primes = set()

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            semi_prime = primes[i] * primes[j]
            if semi_prime <= input_number:
                semi_primes.add(semi_prime)
            else:
                break

    result = len(semi_primes)
    
    return result

# Example usage:
input_value = int(input())
print(count_semi_prime_numbers(input_value))
