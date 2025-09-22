# Function to count and print the number of prime numbers up to a given upper limit
def count_primes():
    # Get the upper limit for the range of numbers to check for primes
    upper_limit = int(input())

    # Initialize a counter for prime numbers
    prime_count = 0

    # Loop through each integer from 1 to upper_limit
    for number in range(1, upper_limit + 1):
        # Initialize a counter for the number of factors
        factor_count = 0

        # Create a variable to hold the current number being checked
        current_number = number

        # Check for factors starting from 2 up to (but not including) the current number
        for factor in range(2, current_number):
            # Determine if the current number is divisible by the factor
            if current_number % factor == 0:
                # Increment the factor count since it's a factor
                factor_count += 1

                # Divide the current number by the factor as long as it is divisible
                while current_number % factor == 0:
                    current_number //= factor

        # A number is prime if it has exactly 2 factors: 1 and itself
        if factor_count == 2:
            # Increment the prime count
            prime_count += 1

    # Output the total number of prime numbers found
    print(prime_count)

# Example of how to run the function
count_primes()
