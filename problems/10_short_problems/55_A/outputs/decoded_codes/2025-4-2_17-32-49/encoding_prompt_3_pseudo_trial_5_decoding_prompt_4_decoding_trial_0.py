def check_primality():
    # Accept an integer input representing the size of the list
    total_numbers = int(input())
    
    # Initialize an array of booleans set to True
    is_prime_array = [True] * total_numbers
    
    # Initialize variables for tracking positions
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
    remaining_primes = [i for i in is_prime_array if i]

    # Check if there are any True values remaining
    if len(remaining_primes) == 0:
        print('YES')  # Indicate that no primes remain
    else:
        print('NO')   # Indicate that some primes remain

# Call the function to execute
check_primality()
