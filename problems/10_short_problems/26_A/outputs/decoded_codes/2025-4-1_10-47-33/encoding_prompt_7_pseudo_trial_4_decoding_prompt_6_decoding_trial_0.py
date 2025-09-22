def count_semi_prime_numbers(input_number):
    # Initialize the result to count semi-prime numbers
    semi_prime_count = 0
    
    # Loop through each integer from 1 to input_number
    for current_integer in range(1, input_number + 1):
        # Initialize the count of prime factors for the current integer
        prime_factor_count = 0
        current_number = current_integer
        
        # Check for factors starting from 2 to current_integer - 1
        for factor in range(2, current_integer):
            # If current number is divisible by the factor
            if current_number % factor == 0:
                # Increment the prime factor count
                prime_factor_count += 1
                
                # While current_number is divisible by factor
                while current_number % factor == 0:
                    # Divide current_number by the factor
                    current_number //= factor
                
        # If exactly two prime factors were found
        if prime_factor_count == 2:
            # Increment the semi-prime count
            semi_prime_count += 1
            
    # Return the final count of semi-prime numbers
    return semi_prime_count

# Read input from user
input_number = int(input())

# Call the function and print the result
result = count_semi_prime_numbers(input_number)
print(result)
