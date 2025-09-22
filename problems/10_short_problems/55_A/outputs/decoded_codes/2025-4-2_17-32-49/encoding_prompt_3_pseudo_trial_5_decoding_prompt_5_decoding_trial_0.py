# Function to determine if there are any prime-like positions remaining
def check_prime_positions():
    # Accept an integer input for the size of the list
    total_numbers = int(input())
    
    # Initialize a list of boolean values set to True
    is_prime_array = [True] * total_numbers
    
    # Variables for tracking positions
    position_increment = 1
    current_index = 0
    
    # Process through a range to determine prime-like positions
    while position_increment <= 500000:
        # If the current boolean position is still True
        if is_prime_array[current_index]:
            # Mark this position as False
            is_prime_array[current_index] = False
        
        # Increment the position increment
        position_increment += 1
        
        # Calculate the next index to mark in a circular manner
        current_index = (current_index + position_increment) % total_numbers
    
    # Filter the list for positions that are still marked as True
    remaining_primes = [index for index, value in enumerate(is_prime_array) if value]

    # Check if there are any True values remaining
    if len(remaining_primes) == 0:
        print('YES')  # Indicate that no primes remain
    else:
        print('NO')   # Indicate that some primes remain

# Example of running the function
# check_prime_positions()

# Note: Uncomment the last line to test the function with input.
