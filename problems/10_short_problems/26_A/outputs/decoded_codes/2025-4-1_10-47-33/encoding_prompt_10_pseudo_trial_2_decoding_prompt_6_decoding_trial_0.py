# Step 1: Read the input value
t = int(input())  # Get the upper limit from the user as an integer

# Step 2: Initialize result counter
result_counter = 0

# Step 3: Loop through each integer from 1 to t
for i in range(1, t + 1):  # Looping from 1 to t
    # Step 4: Initialize prime factor counter
    prime_factor_count = 0
    num = i  # Store current value of i in num

    # Step 5: Check for factors of num
    for j in range(2, i):  # Checking factors from 2 to (i - 1)
        if num % j == 0:  # Check if j is a factor of num
            # Increment count of prime factors
            prime_factor_count += 1

            # Step 6: Remove all occurrences of the factor j from num
            while num % j == 0:  # While j is a factor, remove it
                num //= j  # Remove factor j by dividing

    # Step 7: Check if the count of prime factors equals 2
    if prime_factor_count == 2:  # Check if there are exactly two prime factors
        # Step 8: Increment the result counter for each valid i
        result_counter += 1  # Count this number as valid

# Step 9: Output the result
print(result_counter)  # Print the total count of numbers with exactly two prime factors
