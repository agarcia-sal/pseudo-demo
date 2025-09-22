def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read the upper limit from user input
    t = int(input())

    # Step 2: Initialize a variable to count numbers with exactly two distinct prime factors
    result = 0

    # Step 3: Loop through each integer from 1 to t (inclusive)
    for i in range(1, t + 1):
        count = 0  # Variable to count distinct prime factors
        number = i  # Temporary variable for factorization

        # Step 3.1: Check for prime factors starting from 2 to one less than i
        for j in range(2, i):
            if number % j == 0:  # If j is a factor of number
                count += 1  # Increment count of distinct prime factors
                
                # Step 3.2: Remove all instances of this factor
                while number % j == 0:
                    number //= j  # Divide number by j completely

        # Step 4: Check if count equals 2
        if count == 2:
            result += 1  # Increment result count

    # Step 5: Print the result
    print(result)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
