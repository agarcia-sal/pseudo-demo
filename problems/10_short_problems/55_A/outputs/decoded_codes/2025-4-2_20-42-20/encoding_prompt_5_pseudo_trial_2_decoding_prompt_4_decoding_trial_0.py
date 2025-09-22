def main():
    # Step 2: Retrieve Input
    n = int(input())  # Read the size of the list

    # Step 3: Initialize List
    status = [True] * n  # Create a list with n elements, all set to True

    # Step 4: Initialize Variables
    index = 0  # Tracks the current position in the list
    increment = 1  # Determines the progression through the list

    # Step 5: Perform Modifications
    while increment <= 500000:
        if status[index]:  # If the current element is active
            status[index] = False  # Mark it as inactive
        increment += 1  # Prepare the next step
        index = (index + increment) % n  # Update index using the formula

    # Step 6: Check Remaining Active Elements
    active_elements = [x for x in status if x]  # Filter for True values

    # Step 7: Determine Output
    if len(active_elements) == 0:  # No active elements
        print("YES")
    else:  # There are still active elements
        print("NO")

# Step 1: Start Program
if __name__ == "__main__":
    main()
