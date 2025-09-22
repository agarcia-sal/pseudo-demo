def main():
    # Step 1: Receive input value for n
    number_of_elements = int(input())
    
    # Step 2: Initialize a boolean list to track elements
    is_active = [True] * number_of_elements
    
    # Step 3: Initialize index variables for the loop
    index = 0
    increment = 1
    
    # Step 4: Loop through numbers while the increment value is less than or equal to 500,000
    while increment <= 500000:
        # Step 5: Check if the current index in the boolean list is active
        if is_active[index]:
            # Step 6: Mark the current index as inactive
            is_active[index] = False
        
        # Step 7: Move to the next increment
        increment += 1
        
        # Step 8: Update the index based on the current increment while ensuring it wraps around
        index = (index + increment) % number_of_elements
    
    # Step 9: Create a list of active elements from the boolean list
    active_elements = [i for i, active in enumerate(is_active) if active]
    
    # Step 10: Check if there are active elements left
    if len(active_elements) == 0:
        # Step 11: If no active elements, output 'YES'
        print('YES')
    else:
        # Step 12: Otherwise, output 'NO'
        print('NO')

# Ensure the script runs when executed
if __name__ == "__main__":
    main()
