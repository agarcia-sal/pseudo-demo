# Function to process the active status of numbers based on the given logic
def process_active_numbers():
    # Step 1: Initialize Input
    n = int(input())  # Read an integer n, representing the size of the list
    
    # Step 2: Create a Boolean List
    is_active = [True] * n  # Initialize list with True values
    
    # Step 3: Set Up Variables
    index = 0  # Start index at 0
    counter = 1  # Start counter at 1
    
    # Step 4: Iterate While Counter is Less Than or Equal To 500000
    while counter <= 500000:
        # If current index position is True, set it to False
        if is_active[index]:
            is_active[index] = False
        
        # Increment the counter
        counter += 1
        
        # Update index in a circular manner using modulo operation
        index = (index + counter) % n
    
    # Step 5: Filter Active Elements
    active_elements = [i for i in is_active if i]  # List of still True values
    
    # Step 6: Check Active Elements
    if len(active_elements) == 0:
        print("YES")  # Output "YES" if no active elements
    else:
        print("NO")  # Output "NO" if there are active elements

# Uncomment to run the function
# process_active_numbers()
