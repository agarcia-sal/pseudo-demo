# Step 1: Read total number of test cases 
number_of_test_cases = int(input())

# Step 2: Initialize result variable to count numbers with exactly two distinct prime factors
count_with_two_distinct_primes = 0

# Step 3: Loop through each number from 1 to the number of test cases inclusive
for current_number in range(1, number_of_test_cases + 1):
    # Initialize a variable to count distinct prime factors for the current number
    count_of_distinct_primes = 0
    # We will check for prime factors starting from 2
    possible_divisor = 2
    
    # Factor the current number to find distinct prime factors
    while possible_divisor < current_number:
        if current_number % possible_divisor == 0:
            # Found a distinct prime factor
            count_of_distinct_primes += 1
            
            # Remove all occurrences of this prime factor
            while current_number % possible_divisor == 0:
                current_number //= possible_divisor
        
        # Move to the next possible divisor
        possible_divisor += 1
        
    # Check if the number has exactly two distinct prime factors
    if count_of_distinct_primes == 2:
        count_with_two_distinct_primes += 1

# Step 4: Output the final count of numbers with exactly two distinct prime factors
print(count_with_two_distinct_primes)
