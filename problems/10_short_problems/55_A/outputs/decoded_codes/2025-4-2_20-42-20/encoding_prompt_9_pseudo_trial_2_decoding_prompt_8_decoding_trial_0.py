def main():
    # Step 2: Receive Input
    total_positions = int(input())

    # Step 3: Initialize List
    positions = [True] * total_positions

    # Step 4: Set Initial Indices
    current_index = 0
    step = 1

    # Step 5: Iterate through Marking Process
    while step <= 500000:
        if positions[current_index]:
            positions[current_index] = False  # Mark position as False

        step += 1
        current_index = (current_index + step) % total_positions  # Update current index

    # Step 6: Check for Unmarked Positions
    remaining_unmarked = [pos for pos in positions if pos]

    # Step 7: Determine Result
    if not remaining_unmarked:
        print("YES")  # All positions marked
    else:
        print("NO")   # Some positions remain unmarked

# Step 1: Start of Program
main()
