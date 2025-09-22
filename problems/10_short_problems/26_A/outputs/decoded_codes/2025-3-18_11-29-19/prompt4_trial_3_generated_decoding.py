def count_semiprimes(t):
    # Initialize a counter for the number of semiprime numbers
    semiprime_count = 0

    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize a count for distinct prime factors
        distinct_prime_factors = 0
        num = i

        # Loop through possible factors from 2 to the number itself
        for j in range(2, i):
            if num % j == 0:  # Check if j is a factor of num
                distinct_prime_factors += 1  # Increment the distinct prime factor count
                
                # Divide num by j as long as it is a factor
                while num % j == 0:
                    num //= j  # Floor division to remove the factor completely

        # Check if the number has exactly two distinct prime factors
        if distinct_prime_factors == 2:
            semiprime_count += 1  # Increment the semiprime counter

    return semiprime_count  # Return the count of semiprime numbers

# Read an integer input representing the upper limit
t = int(input())

# Print the count of semiprime numbers
print(count_semiprimes(t))
