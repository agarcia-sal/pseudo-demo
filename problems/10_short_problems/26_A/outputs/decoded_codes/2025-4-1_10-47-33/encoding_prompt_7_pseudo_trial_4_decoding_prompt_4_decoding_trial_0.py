def count_semi_prime_numbers(input_number):
    # Initialize the result to count semi-prime numbers
    result = 0
    
    # Iterate through each integer from 1 to input_number
    for current_number in range(1, input_number + 1):
        # Count of unique prime factors
        prime_factor_count = 0
        temp_number = current_number  # Store the current number to modify
        
        # Check for prime factors from 2 to current_number - 1
        for i in range(2, current_number):
            # If i is a prime factor of current_number
            if temp_number % i == 0:
                prime_factor_count += 1  # Increment count of prime factors
                
                # Divide temp_number by i until it is no longer divisible
                while temp_number % i == 0:
                    temp_number //= i
        
        # If there are exactly 2 prime factors, it's a semi-prime
        if prime_factor_count == 2:
            result += 1  # Increment the semi-prime result count
    
    return result  # Return the total count of semi-prime numbers


print(count_semi_prime_numbers(10))  # Expected output: 4 (Semi-primes: 4, 6, 9, 10)
print(count_semi_prime_numbers(20))  # Expected output: 8 (Semi-primes: 4, 6, 9, 10, 14, 15, 21, 25)
print(count_semi_prime_numbers(1))   # Expected output: 0 (No semi-primes below 1)
print(count_semi_prime_numbers(0))   # Expected output: 0 (No semi-primes below or equal to 0)
print(count_semi_prime_numbers(2))   # Expected output: 0 (No semi-primes below 2)
print(count_semi_prime_numbers(4))   # Expected output: 1 (Only semi-prime: 4)
