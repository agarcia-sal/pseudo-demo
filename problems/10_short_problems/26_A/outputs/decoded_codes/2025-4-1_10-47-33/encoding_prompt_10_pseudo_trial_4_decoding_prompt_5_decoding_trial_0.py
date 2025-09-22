# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Step 2: Input Number of Test Cases
    test_cases = int(input())
    
    # Step 3: Initialize Result Counter
    result_count = 0  # This will hold the count of numbers with exactly two distinct prime factors

    # Step 4: Loop Through Each Number from 1 to test_cases
    for current_number in range(1, test_cases + 1):
        # Initialize counter for distinct prime factors
        distinct_prime_count = 0
        num = current_number  # To factorize current number
        
        # Step 5: Loop to Find Factors
        for factor in range(2, current_number):
            # Check if factor is a prime factor of num
            if num % factor == 0:
                distinct_prime_count += 1  # Found a new distinct prime factor
                # While num is divisible by factor
                while num % factor == 0:
                    num //= factor  # Divide num by factor until it no longer divides

        # Step 6: Check for Prime Condition
        if distinct_prime_count == 2:  # Check if current_number has exactly two distinct prime factors
            result_count += 1  # Count this number as valid

    # Step 7: Output Result
    print(result_count)  # Print the total count of valid numbers

# Call the function to execute the program
count_numbers_with_two_distinct_prime_factors()
