# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read the upper limit from user input
    t = int(input())
    
    # Step 2: Initialize the result counter
    result = 0
    
    # Step 3: Loop through each integer from 1 to t (inclusive)
    for i in range(1, t + 1):
        # Initialize a counter for the number of distinct prime factors
        count = 0
        current_number = i  # Step 4: Work with the current number
        
        # Step 4: Check for prime factors
        for j in range(2, i):  # Check for factors from 2 to i-1
            if current_number % j == 0:  # If j is a factor of current_number
                count += 1  # Found a new prime factor
                # Remove all occurrences of j from current_number
                while current_number % j == 0:
                    current_number //= j
        
        # Step 5: If exactly two distinct prime factors were found
        if count == 2:
            result += 1  # Increment the result
    
    # Step 6: Output the final count
    print(result)

# Call the function to execute the counting
count_numbers_with_two_distinct_prime_factors()
