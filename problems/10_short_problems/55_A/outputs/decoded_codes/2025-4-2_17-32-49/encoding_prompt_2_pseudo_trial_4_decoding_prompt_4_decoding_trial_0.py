def mark_positions():
    # Step 2: Input
    n = int(input())
    
    # Step 3: Initialize
    is_available = [True] * n
    position = 0
    step = 1

    # Step 4: Loop until step exceeds 500,000
    while step <= 500000:
        if is_available[position]:
            is_available[position] = False  # Mark this position as unavailable
        step += 1
        position = (position + step) % n  # Wrap around the list

    # Step 5: Check for available positions
    available_positions = [i for i in is_available if i]

    # Step 6: Output Result
    if len(available_positions) == 0:
        print("YES")  # All positions are marked unavailable.
    else:
        print("NO")   # Some positions are still available.

# Function call to execute the solution
mark_positions()
