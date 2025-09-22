# Function to count how many numbers from 1 to targetNumber are exactly the product of two distinct prime numbers
def count_distinct_prime_products():
    # Step 1: Accept the target number from user input
    target_number = int(input())
    
    # Step 2: Initialize a counter for valid numbers
    valid_count = 0
    
    # Step 3: Loop through each number starting from 1 to the target number
    for current_number in range(1, target_number + 1):
        # Initialize a counter for the number of distinct prime factors
        distinct_prime_count = 0
        
        # Store the current number to check its prime factors
        check_number = current_number
        
        # Step 4: Check for prime factors starting from 2 up to current_number - 1
        for potential_prime in range(2, current_number):
            # If potential_prime is a factor of check_number
            if check_number % potential_prime == 0:
                distinct_prime_count += 1  # Increment the distinct prime factors counter
                
                # Step 5: Divide check_number by potentialPrime until it is no longer divisible
                while check_number % potential_prime == 0:
                    check_number //= potential_prime  # Update check_number
                
        # Step 6: Check if the current number has exactly two distinct prime factors
        if distinct_prime_count == 2:
            valid_count += 1  # Increment the count of valid numbers

    # Step 7: Output the total count of numbers with exactly two distinct prime factors
    print(valid_count)

# Call the function to execute the counting process
count_distinct_prime_products()
