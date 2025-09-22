# Step 1: Declare and initialize variables
test_cases = 0  # Number of test cases
result_count = 0  # Result count to hold numbers with exactly two prime factors

# Step 2: Input number of test cases
test_cases = int(input())  # Read the number of test cases

# Step 3: Loop through each number from 1 to test_cases
for current_number in range(1, test_cases + 1):  
    factor_count = 0  # Initialize the count of distinct prime factors
    num = current_number  # Set current number for factor checking

    # Step 4: Check for factors of the current number
    for divisor in range(2, current_number):  
        if num % divisor == 0:  # If num is divisible by divisor
            factor_count += 1  # Increment the distinct prime factors count

            # Step 5: Divide num by divisor as long as it's divisible
            while num % divisor == 0:  
                num //= divisor  # Reduce num by dividing by the prime factor

    # Step 6: Check if the number has exactly two prime factors
    if factor_count == 2:  
        result_count += 1  # Increment result count if the condition is met

# Step 7: Output the result
print(result_count)  # Print the final count of numbers with exactly two prime factors
