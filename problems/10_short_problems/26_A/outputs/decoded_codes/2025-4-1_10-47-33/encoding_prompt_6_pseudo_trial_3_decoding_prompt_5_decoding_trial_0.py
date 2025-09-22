# Function to count numbers with exactly two unique prime factors up to a given limit
def count_numbers_with_two_unique_prime_factors():
    # Read the integer input that represents the upper limit for checking prime numbers
    upper_limit = int(input())
    
    # Initialize a variable to keep track of the count of numbers with exactly two unique prime factors
    unique_prime_factors_count = 0

    # Loop through each number from 1 to upper_limit (inclusive)
    for i in range(1, upper_limit + 1):
        # Initialize a counter to track the number of unique prime factors for the current number
        current_unique_factors_count = 0
        
        # Create a variable 'current_number' and set it to the current number 'i'
        current_number = i
        
        # Check for potential prime factors starting from 2 up to current_number - 1
        for j in range(2, current_number):
            # If j is a factor of current_number
            if current_number % j == 0:
                # Increment the count of unique prime factors
                current_unique_factors_count += 1
                
                # Divide current_number by j until it is no longer divisible by j
                while current_number % j == 0:
                    current_number //= j

        # After checking all factors, if the count of unique prime factors is exactly 2
        if current_unique_factors_count == 2:
            # Increment the prime count, indicating 'i' has exactly two unique prime factors
            unique_prime_factors_count += 1

    # Output the total count of numbers found with exactly two unique prime factors
    print(unique_prime_factors_count)

# Function call to execute the code (uncomment the line below to run)
# count_numbers_with_two_unique_prime_factors()
