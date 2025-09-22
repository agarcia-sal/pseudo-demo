def count_special_numbers():
    # Read an integer input representing the upper limit for checking
    upper_limit = int(input())
    
    # Initialize a variable to count the special numbers
    special_count = 0
    
    # Loop through each number from 1 to upper_limit
    for number in range(1, upper_limit + 1):
        # Initialize a counter for distinct prime factors
        prime_factor_count = 0
        num = number
        
        # Check for prime factors from 2 up to num
        for factor in range(2, number):
            # If factor is a prime factor of num
            if num % factor == 0:
                # Increment the prime factor counter
                prime_factor_count += 1
                
                # Divide num by factor until factor is no longer a factor
                while num % factor == 0:
                    num //= factor
                    
        # Check if the number has exactly two distinct prime factors
        if prime_factor_count == 2:
            # Increment the special number count
            special_count += 1
            
    # Output the total count of special numbers found
    print(special_count)

# Call the function to execute
count_special_numbers()
