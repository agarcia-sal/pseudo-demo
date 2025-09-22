def count_numbers_with_two_unique_prime_factors():
    # Read an integer input that represents the upper limit for checking numbers
    t = int(input())
    
    # Initialize a variable to keep track of the count of numbers with two unique prime factors
    prime_count = 0

    # Loop through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        # Initialize a counter for the number of unique prime factors for the current number
        unique_prime_factors_count = 0
        
        # Set the current number to 'i'
        current_number = i
        
        # Check for potential prime factors starting from 2 up to current_number
        for j in range(2, current_number):
            if current_number % j == 0:  # If 'j' is a factor of 'current_number'
                unique_prime_factors_count += 1  # Increment the count of unique prime factors
                
                # Divide 'current_number' by 'j' until it is no longer divisible by 'j'
                while current_number % j == 0:
                    current_number //= j
                    
        # If the count of unique prime factors is exactly 2, increment the prime count
        if unique_prime_factors_count == 2:
            prime_count += 1

    # Output the total count of numbers with two unique prime factors
    print(prime_count)

# Call the function to run the program
count_numbers_with_two_unique_prime_factors()
