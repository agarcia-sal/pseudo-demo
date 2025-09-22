def main():
    # Step 1: Get the number of positions in a circular list
    n = int(input())
    
    # Step 2: Initialize the marked list with True (unmarked)
    marked = [True] * n
    
    # Step 3: Set initial variables
    current_index = 0  # to track current position
    step = 1           # will determine the steps for marking
    
    # Step 4: Mark unmarked positions
    while step <= 500000:
        if marked[current_index]:
            marked[current_index] = False  # mark the current position
            
        # Update the current index and step size
        current_index = (current_index + step) % n
        step += 1  # increase the step for the next marking
        
    # Step 5: Check for unmarked positions
    unmarked_positions = [position for position in marked if position]
    
    # Step 6: Determine output based on unmarked positions
    if not unmarked_positions:
        print("YES")  # All positions were marked
    else:
        print("NO")   # There are unmarked positions

# Entry point of the program
if __name__ == "__main__":
    main()
