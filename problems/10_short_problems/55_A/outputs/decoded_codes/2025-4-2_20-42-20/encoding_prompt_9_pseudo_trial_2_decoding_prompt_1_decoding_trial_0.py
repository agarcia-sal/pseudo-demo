# 1. Start of Program

# 2. Receive Input:
total_positions = int(input())

# 3. Initialize List:
positions = [True] * total_positions  # Each entry is initially unmarked (True)

# 4. Set Initial Indices:
current_index = 0
step = 1

# 5. Iterate through Marking Process:
while step <= 500000:
    if positions[current_index] == True:  # If the position is unmarked
        positions[current_index] = False  # Mark the position as False
    
    step += 1
    current_index = (current_index + step) % total_positions  # Calculate the next position

# 6. Check for Unmarked Positions:
remaining_unmarked = [pos for pos in positions if pos]

# 7. Determine Result:
if not remaining_unmarked:  # If remaining_unmarked is empty
    print("YES")  # No unmarked positions remain
else:
    print("NO")  # There are still unmarked positions

# 8. End of Program
