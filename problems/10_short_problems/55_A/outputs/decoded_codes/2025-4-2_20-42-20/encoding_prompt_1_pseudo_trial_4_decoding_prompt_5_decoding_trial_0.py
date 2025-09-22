def mark_positions():
    # Read the number of elements
    n = int(input())
    
    # Initialize a list 'b' of size 'n' with all values set to True
    marked_positions = [True] * n
    
    # Initialize indices
    j = 0  # This will track the current index
    i = 1  # This will start at 1 and increment
    
    # Loop while 'i' is less than or equal to 500,000
    while i <= 500000:
        # Check if the current position in 'marked_positions' is True
        if marked_positions[j]:
            # Mark the position as False
            marked_positions[j] = False
        
        # Increment 'i' by 1
        i += 1
        
        # Update 'j' to the next position, wrapping around using modulo
        j = (j + i) % n
    
    # Extract positions that remain True into a new list 'x'
    unmarked_positions = [pos for pos in marked_positions if pos]
    
    # Check if 'x' is empty
    if len(unmarked_positions) == 0:
        # If empty, print "YES"
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Example of how you could call the function
# mark_positions()  # Uncomment to use
