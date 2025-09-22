def main():
    # Step 2: Retrieve Input
    n = int(input())
    
    # Step 3: Initialize List
    status = [True] * n  # Create a list of `n` elements all set to True
    
    # Step 4: Initialize Variables
    index = 0  # Track the current position in the list
    increment = 1  # Determines the progression through the list

    # Step 5: Perform Modifications
    while increment <= 500000:
        if status[index]:  # If the current element is active
            status[index] = False  # Mark it as inactive

        # Prepare for the next step
        increment += 1  # Increase the increment
        index = (index + increment) % n  # Update index, wrapping around using modulo

    # Step 6: Check Remaining Active Elements
    active_elements = [element for element in status if element]  # Collect all True values

    # Step 7: Determine Output
    if len(active_elements) == 0:  # If no elements are active
        print("YES")  # All elements are inactive
    else:
        print("NO")  # There are still active elements

# Execute the main function
if __name__ == "__main__":
    main()
