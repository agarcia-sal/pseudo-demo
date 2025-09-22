def mark_positions():
    # Step 1: Input
    n = int(input().strip())

    # Step 2: Initialization
    is_present = [True] * n
    index = 0
    step = 1

    # Step 3: Processing Loop
    while step <= 500000:
        if is_present[index]:
            is_present[index] = False  # Mark position as not available
        step += 1
        index = (index + step) % n  # Calculate the next position

    # Step 4: Checking Results
    available_positions = [pos for pos in is_present if pos]

    if len(available_positions) == 0:
        print("YES")  # All positions are marked as not available
    else:
        print("NO")   # There are still available positions

# Call the function to execute the logic
mark_positions()
