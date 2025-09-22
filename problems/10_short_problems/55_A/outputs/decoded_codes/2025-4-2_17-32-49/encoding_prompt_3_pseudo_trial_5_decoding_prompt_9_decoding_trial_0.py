# Accept an integer input representing the size of the list
total_numbers = int(input())
is_prime_array = [True] * total_numbers  # Initialize the list of boolean values

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
remaining_primes = [index for index, value in enumerate(is_prime_array) if value]

# Check if there are any True values remaining
if len(remaining_primes) == 0:
    print('YES')  # Indicate that no primes remain
else:
    print('NO')   # Indicate that some primes remain
