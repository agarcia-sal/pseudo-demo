def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read the upper limit 't' from user input
    t = int(input())
    
    # Step 2: Initialize result to count numbers meeting the criteria
    result = 0
    
    # Step 3: Iterate through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        count = 0  # Variable to track distinct prime factors
        currentNumber = i  # Number to be analyzed for prime factors
        
        # Step 4: Check for prime factors from 2 to i-1
        for j in range(2, i):
            if currentNumber % j == 0:  # j is a prime factor
                count += 1  # Found a distinct prime factor
                
                # Step 4.1: Remove all occurrences of this prime factor
                while currentNumber % j == 0:
                    currentNumber //= j
        
        # Step 5: Check if we found exactly two distinct prime factors
        if count == 2:
            result += 1  # Increment result for number with exactly two distinct prime factors
    
    # Step 6: Output the final result
    print(result)

# Call the function to execute the code
count_numbers_with_two_distinct_prime_factors()
