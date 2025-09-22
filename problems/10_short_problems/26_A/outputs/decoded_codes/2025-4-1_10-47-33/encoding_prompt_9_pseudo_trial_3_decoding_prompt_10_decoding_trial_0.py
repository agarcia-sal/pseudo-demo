def count_semiprimes(t):
    # Initialize a count variable to keep track of semiprime numbers
    semiprime_count = 0

    # Loop through each number from 1 to t (inclusive)
    for current_number in range(1, t + 1):
        distinct_prime_count = 0  # Counter for distinct prime factors
        number = current_number  # Variable to find prime factors

        # Loop through potential factors from 2 to current_number - 1
        for potential_factor in range(2, current_number):
            if number % potential_factor == 0:  # Check divisibility
                distinct_prime_count += 1  # Found a new prime factor

                # While the number is divisible by potential_factor, divide it
                while number % potential_factor == 0:
                    number //= potential_factor
        
        # If exactly two distinct prime factors were found, it's a semiprime
        if distinct_prime_count == 2:
            semiprime_count += 1

    # Output the count of semiprimes found
    return semiprime_count

if __name__ == "__main__":
    t = int(input())  # Read an integer t from the user
    result = count_semiprimes(t)  # Count semiprimes up to t
    print(result)  # Output the result
