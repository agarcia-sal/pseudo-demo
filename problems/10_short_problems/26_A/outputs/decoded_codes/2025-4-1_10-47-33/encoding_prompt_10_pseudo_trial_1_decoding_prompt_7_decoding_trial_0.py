# Function to check for numbers with exactly two distinct prime factors
def count_numbers_with_two_prime_factors():
    # Step 1: Declare and initialize variables
    t = int(input())  # Input number of test cases
    res = 0           # Result variable to count numbers with exactly two prime factors

    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0      # Counter for distinct prime factors
        num = i      # Current number to analyze

        # Step 4: Check for factors of the current number
        for j in range(2, i):  # Checking for factors from 2 to i-1
            if num % j == 0:   # If j is a factor of num
                cnt += 1       # Increment the count of distinct prime factors

                # Step 5: Divide num by j as long as it's divisible
                while num % j == 0:  # While divisible by j, keep dividing
                    num //= j       # Perform integer division to reduce num
            # No need for an else part since we're only interested in factors

        # Step 6: Check if the number has exactly two prime factors
        if cnt == 2:  # If there are exactly two distinct prime factors
            res += 1   # Increment the result count

    # Step 7: Output the result
    print(res)  # Print the result

# Execute the function
count_numbers_with_two_prime_factors()
