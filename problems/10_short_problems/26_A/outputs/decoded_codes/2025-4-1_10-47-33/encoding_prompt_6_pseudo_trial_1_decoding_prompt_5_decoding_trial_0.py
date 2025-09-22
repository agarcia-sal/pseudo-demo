# Function to count numbers with exactly two unique prime factors
def count_numbers_with_two_unique_prime_factors():
    # Read an integer value 't' from the user
    t = int(input())
    # Initialize a variable 'result' to track numbers with two unique prime factors
    result = 0
    
    # Iterate over each integer 'i' from 1 to 't' (inclusive)
    for i in range(1, t + 1):
        # Initialize a count variable to count unique prime factors
        count = 0  
        current_number = i  # Set 'current_number' to 'i'

        # Check divisibility from 2 up to 'i - 1'
        for j in range(2, i):
            # If 'current_number' is divisible by 'j'
            if current_number % j == 0:
                count += 1  # Found a new unique prime factor
                
                # Reduce 'current_number' by dividing out 'j' until it's no longer divisible
                while current_number % j == 0:
                    current_number //= j

        # Check if exactly two unique prime factors were found
        if count == 2:
            result += 1  # Increment the result
    
    # Output the value of 'result'
    print(result)

# Call the function to execute
count_numbers_with_two_unique_prime_factors()
