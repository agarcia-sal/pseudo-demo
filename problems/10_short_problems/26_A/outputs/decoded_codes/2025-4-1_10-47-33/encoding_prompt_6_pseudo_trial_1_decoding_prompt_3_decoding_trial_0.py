def count_numbers_with_two_unique_prime_factors():
    # Step 2: Read input from the user
    t = int(input())
    
    # Step 3: Initialize a result variable to zero
    result = 0

    # Step 4: Loop through each integer from 1 to t (inclusive)
    for i in range(1, t + 1):
        count = 0        # Step 4a: Initialize count for unique prime factors
        current_number = i  # Step 4b: Set current number to i
        
        # Step 5: Check for factors from 2 to (i - 1)
        for j in range(2, i):
            # Step 5a: Check if current_number is divisible by j
            if current_number % j == 0:
                count += 1  # Step 5b.i: Increment count for found prime factor
                
                # Step 5b.ii: Remove all instances of j from current_number
                while current_number % j == 0:
                    current_number //= j

        # Step 6: Check if count of unique prime factors is exactly 2
        if count == 2:
            result += 1  # Step 6a: Increment result if condition is met

    # Step 7: Output the total count of numbers with exactly two unique prime factors
    print(result)

# Call the function to execute the program
count_numbers_with_two_unique_prime_factors()
