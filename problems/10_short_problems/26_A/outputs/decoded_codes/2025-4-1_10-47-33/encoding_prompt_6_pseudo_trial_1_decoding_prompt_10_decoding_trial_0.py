def count_numbers_with_two_unique_prime_factors():
    # Step 2: Read an integer value 't' from the user
    t = int(input())
    result = 0  # Step 3: Initialize the result variable to zero

    # Step 4: For each integer 'i' from 1 to 't' (inclusive)
    for i in range(2, t + 1):  # start from 2 as 1 has no prime factors
        count = 0  # Step 4a: Initialize count variable to zero
        current_number = i  # Step 4b: Set currentNumber to i

        # Step 5: For each integer 'j' from 2 to (i - 1)
        for j in range(2, int(i**0.5) + 1):  # Only need to check up to sqrt(i)
            if current_number % j == 0:  # Step 5a: Check if divisible
                count += 1  # Step 5b.i: Increment count by 1
                # Step 5b.ii: While currentNumber is divisible by j
                while current_number % j == 0:
                    current_number //= j  # Remove the factor
        # If there's any prime factor greater than sqrt(i), it will be current_number here
        if current_number > 1:
            count += 1  # Consider the remaining prime factor if > 1

        # Step 6: If count is equal to 2, increment result
        if count == 2:
            result += 1

    # Step 7: Output the value of result
    print(result)  # Output the total count

# Start the program
count_numbers_with_two_unique_prime_factors()
