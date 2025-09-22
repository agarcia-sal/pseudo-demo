# Function to count semiprimes up to a given number t
def count_semiprimes():
    # Read an integer from the user representing the upper limit
    t = int(input())
    
    # Initialize a count for semiprime numbers
    semiprime_count = 0
    
    # Loop through each number from 1 to t (inclusive)
    for current_number in range(1, t + 1):
        # Initialize the distinct prime factors count
        distinct_prime_count = 0
        # Set a variable to find prime factors
        number = current_number
        
        # Loop through potential factors starting from 2
        for potential_factor in range(2, current_number):
            # Check if the current number is divisible by potential_factor
            if number % potential_factor == 0:
                # A new prime factor is found
                distinct_prime_count += 1
                # Divide number by potential_factor while it's divisible
                while number % potential_factor == 0:
                    number //= potential_factor
        
        # Check if the number has exactly two distinct prime factors
        if distinct_prime_count == 2:
            semiprime_count += 1
    
    # Output the count of semiprime numbers found
    print(semiprime_count)

# Call the function to execute
count_semiprimes()
