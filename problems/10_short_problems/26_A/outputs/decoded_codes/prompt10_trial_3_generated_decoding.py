def count_prime_numbers():
    # Step 1: Get the integer input for the upper limit of prime number checking
    t = int(input())

    # Step 2: Initialize result variable to hold the count of numbers with exactly two unique prime factors
    prime_count = 0

    # Step 3: Iterate through each integer from 1 to t inclusive
    for i in range(1, t + 1):
        unique_factors_count = 0  # Counts the number of unique prime factors
        num = i  # The current number being analyzed

        # Step 4: Check for factors from 2 to (i - 1)
        for j in range(2, i):
            if num % j == 0:  # If j is a divisor of num
                unique_factors_count += 1  # Found a new unique prime factor
                # Remove all occurrences of j from num
                while num % j == 0:
                    num //= j  # Perform integer division

        # Step 5: Check if the number has exactly 2 unique prime factors
        if unique_factors_count == 2:
            prime_count += 1  # Update the count of prime-like numbers

    # Step 6: Print the total count
    print(prime_count)

# Call the function to execute
count_prime_numbers()
