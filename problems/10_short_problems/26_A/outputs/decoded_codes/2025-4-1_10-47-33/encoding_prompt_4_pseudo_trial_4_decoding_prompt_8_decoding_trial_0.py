def count_prime_like_numbers():
    # Read the total number of integers to process
    total_numbers = int(input())

    # Initialize the result counter for prime-like numbers
    prime_count = 0

    # Loop through each number from 1 to total_numbers
    for current_number in range(1, total_numbers + 1):
        # Initialize a counter for distinct prime factors
        distinct_prime_factors_count = 0
        number = current_number

        # Check for prime factors from 2 to current_number - 1
        for possible_prime_factor in range(2, current_number):
            # If possible_prime_factor is a divisor of number
            if number % possible_prime_factor == 0:
                # Increment the distinct prime factors count
                distinct_prime_factors_count += 1

                # Divide number by possiblePrimeFactor until it no longer divides evenly
                while number % possible_prime_factor == 0:
                    number //= possible_prime_factor

        # If there are exactly 2 distinct prime factors, count this number as a prime-like number
        if distinct_prime_factors_count == 2:
            prime_count += 1

    # Output the total count of numbers with exactly 2 distinct prime factors
    print(prime_count)

# Call the function to execute the program
count_prime_like_numbers()
