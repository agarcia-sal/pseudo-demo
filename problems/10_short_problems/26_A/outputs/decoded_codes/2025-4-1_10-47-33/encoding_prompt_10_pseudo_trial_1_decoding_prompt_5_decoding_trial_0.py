# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_prime_factors():
    # Step 1: Declare and initialize variables
    t = 0  # Number of test cases
    res = 0  # Result count

    # Step 2: Input number of test cases
    t = int(input())  # Read number of cases

    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0  # Count of distinct prime factors
        num = i  # Current number being checked

        # Step 4: Check for factors of the current number
        for j in range(2, i):  # Check factors from 2 to i - 1
            if num % j == 0:  # Is j a factor of num?
                cnt += 1  # Increment the count of distinct prime factors
                
                # Step 5: Divide num by j as long as it's divisible
                while num % j == 0:
                    num //= j  # Reduce num by the factor j

        # Step 6: Check if the number has exactly two prime factors
        if cnt == 2:
            res += 1  # Increment result count

    # Step 7: Output the result
    return res  # Return the final count

# The count function can be called to obtain results
result = count_numbers_with_two_prime_factors()
print(result)  # Output the result
