# Function to process the given pseudocode logic
def process_array(n):
    # Step 2: Initialize the boolean array with True values
    is_processed = [True] * n
    
    # Step 3: Set initial variables
    current_index = 0
    increment = 1
    
    # Step 4: Loop to process the array
    while increment <= 500000:
        if is_processed[current_index]:  # Check if the current index is still True
            is_processed[current_index] = False  # Mark it as processed
        
        increment += 1  # Increment the step
        current_index = (current_index + increment) % n  # Update current index with wrap-around
    
    # Step 5: Create a list of remaining True values
    remaining_true = [value for value in is_processed if value]
    
    # Step 6: Output results based on remaining elements
    if len(remaining_true) == 0:
        print("YES")  # All elements processed
    else:
        print("NO")  # There are unprocessed elements

# Input reading
n = int(input())  # Read the size of the array from user
process_array(n)  # Call the function
