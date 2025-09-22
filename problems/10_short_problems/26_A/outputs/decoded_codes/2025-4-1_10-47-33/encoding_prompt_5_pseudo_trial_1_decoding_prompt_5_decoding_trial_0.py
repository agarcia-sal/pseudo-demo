# Function to count semiprime numbers up to a specified upper limit
def count_semiprime_numbers():
    # Take an integer input which represents the upper limit for counting semiprime numbers
    upper_limit = int(input())
    
    # Initialize a counter to keep track of semiprime numbers found
    semiprime_count = 0
    
    # Loop through each number from 1 to upper limit
    for current_number in range(1, upper_limit + 1):
        prime_factor_count = 0  # Counter for counting distinct prime factors
        temp_number = current_number  # Copy of current number for factorization

        # Loop through all numbers starting from 2 up to the current number to check for factors
        for potential_factor in range(2, temp_number):
            # If the current number is divisible by the potential factor
            if temp_number % potential_factor == 0:
                prime_factor_count += 1  # Increase the distinct prime factors count

                # While it's divisible, continuously divide the current number by this factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # Check if exactly two distinct prime factors were found
        if prime_factor_count == 2:
            semiprime_count += 1  # Found a semiprime number, increase the count

    # Output the total count of semiprime numbers found
    print(semiprime_count)

# Call the function to execute
count_semiprime_numbers()
