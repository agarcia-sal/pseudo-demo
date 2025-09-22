def count_numbers_with_two_prime_factors():
    # Read the input value for 't' as an integer
    t = int(input())

    # Initialize result counter for numbers with exactly two prime factors
    result_count = 0

    # Iterate over each number from 1 to t
    for i in range(1, t + 1):
        # Initialize counter for prime factors
        factor_count = 0
        current_number = i

        # Check for prime factors from 2 up to (i-1)
        for j in range(2, current_number):
            # Check if 'j' is a factor of 'current_number'
            if current_number % j == 0:
                factor_count += 1

                # Divide 'current_number' by 'j' while it is divisible
                while current_number % j == 0:
                    current_number //= j
        
        # If exactly two prime factors are found, count it as a valid case
        if factor_count == 2:
            result_count += 1

    # Output the total count of numbers with exactly two prime factors
    print(result_count)

# Invoke the function to execute the code
count_numbers_with_two_prime_factors()
