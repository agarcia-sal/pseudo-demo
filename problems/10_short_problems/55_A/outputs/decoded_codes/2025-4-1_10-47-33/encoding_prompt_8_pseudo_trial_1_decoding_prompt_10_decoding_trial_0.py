def main():
    # Step 1: Get input for the size of the list
    n = int(input())

    # Step 2: Initialize the list to denote unmarked items
    is_marked = [True] * n

    # Step 3: Initialize counters
    current_index = 0
    increment = 1

    # Step 4: Start the marking process
    while increment <= 500000:
        # Step 4a: Check if the current item is still marked as True
        if is_marked[current_index]:
            # Mark the current item as processed (False)
            is_marked[current_index] = False
        
        # Step 4b: Update increment and current_index for next operation
        increment += 1
        current_index = (current_index + increment) % n

    # Step 5: Check for unmarked items
    unmarked_items = [item for item in is_marked if item]

    # Step 6: Output the result based on unmarked items
    if len(unmarked_items) == 0:
        print('YES')
    else:
        print('NO')

# This allows the code to run when executed directly, but not when imported
if __name__ == "__main__":
    main()
