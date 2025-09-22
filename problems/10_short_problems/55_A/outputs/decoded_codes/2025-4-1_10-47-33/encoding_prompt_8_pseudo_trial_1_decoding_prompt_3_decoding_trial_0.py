def main():
    # Step 2: Get Input
    n = int(input())  # Read an integer value 'n' from user input

    # Step 3: Initialize List
    IsMarked = [True] * n  # List initialized to True, indicating all items are unmarked

    # Step 4: Initialize Counters
    currentIndex = 0  # Track the current index being operated on
    increment = 1     # Step size for marking the list

    # Step 5: Marking Process
    while increment <= 500000:
        if IsMarked[currentIndex]:  # Check if current item is still marked as True
            IsMarked[currentIndex] = False  # Mark this item as processed
        increment += 1  # Increase the step for the next operation
        currentIndex = (currentIndex + increment) % n  # Update index, wrapping around if needed

    # Step 6: Check for Unmarked Items
    UnmarkedItems = [item for item in IsMarked if item]  # Collect items that are still True (unmarked)

    # Step 7: Output Result
    if len(UnmarkedItems) == 0:  # If all items are marked
        print('YES')
    else:  # If there are still unmarked items
        print('NO')

# Step 1: Start Program
if __name__ == "__main__":
    main()  # Call the main function to begin execution
