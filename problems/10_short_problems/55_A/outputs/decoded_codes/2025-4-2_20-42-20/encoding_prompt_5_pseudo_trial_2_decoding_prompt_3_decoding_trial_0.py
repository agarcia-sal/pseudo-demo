def main():
    # Step 2: Retrieve Input
    n = int(input())  # Read the size of the list
    
    # Step 3: Initialize List
    status = [True] * n  # Create a list of `n` elements all set to True
    
    # Step 4: Initialize Variables
    index = 0  # Current position in the list
    increment = 1  # Determines how we progress through the list

    # Step 5: Perform Modifications
    while increment <= 500000:
        if status[index]:  # Check if the current element is active
            status[index] = False  # Mark the current element as inactive
        increment += 1  # Prepare the next step
        index = (index + increment) % n  # Wrap around using modulo

    # Step 6: Check Remaining Active Elements
    active_elements = [element for element in status if element]  # List of remaining True values
    
    # Step 7: Determine Output
    if len(active_elements) == 0:  # All elements are inactive
        print("YES")
    else:  # There are still active elements
        print("NO")

# Invoke the main function
if __name__ == "__main__":
    main()
