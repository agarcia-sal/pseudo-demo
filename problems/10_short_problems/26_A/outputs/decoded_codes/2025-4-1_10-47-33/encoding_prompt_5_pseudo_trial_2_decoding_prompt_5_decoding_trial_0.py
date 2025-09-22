# Function to count prime numbers up to a user-defined integer
def count_primes_up_to_t():
    # Step 1: Get Input
    t = int(input())  # Take an integer input from the user

    # Step 2: Initialize a Counter
    prime_count = 0  # Variable to hold the number of prime numbers found

    # Step 3: Loop Through Each Number
    for current_number in range(1, t + 1):
        divisor_count = 0  # Counter for divisors of the current number
        remaining_value = current_number  # Value to factorize

        # Step 4: Check for Divisibility
        for potential_divisor in range(2, current_number):
            if remaining_value % potential_divisor == 0:
                divisor_count += 1  # Increment divisor count
                # Remove all occurrences of potential_divisor from remaining_value
                while remaining_value % potential_divisor == 0:
                    remaining_value //= potential_divisor  

        # Step 5: Determine if Prime
        if divisor_count == 2:  # Current number is prime if it has exactly 2 divisors
            prime_count += 1  # Increment prime count

    # Step 6: Output Result
    print(prime_count)  # Print the final count of prime numbers found

# Example test cases to consider:
# If t = 10, prime numbers are [2, 3, 5, 7] -> Should output 4
# If t = 1, there are no prime numbers -> Should output 0

# To run the function
count_primes_up_to_t()
