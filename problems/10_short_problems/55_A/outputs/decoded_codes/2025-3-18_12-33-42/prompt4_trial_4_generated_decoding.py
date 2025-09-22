def main():
    # Get input value for n
    n = int(input())
    
    # Initialize a list of boolean values to True
    is_not_deleted = [True] * n

    # Initialize counter variables
    j = 0
    i = 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current position in the list is True
        if is_not_deleted[j]:
            # Mark this position as False (deleted)
            is_not_deleted[j] = False
        
        # Increment the counter
        i += 1
        
        # Update the index j using circular indexing
        j = (j + i) % n
    
    # Filter the list to include only True values
    remaining_items = [value for value in is_not_deleted if value]

    # Check if there are any remaining True values
    if len(remaining_items) == 0:
        print('YES')  # All items were deleted
    else:
        print('NO')   # There are items that were not deleted

if __name__ == "__main__":
    main()
