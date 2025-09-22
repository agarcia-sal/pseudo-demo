# Start

# Receive Input
size = int(input())

# Initialize List
positions = [True] * size

# Set Counters
current_increment = 1
current_position_index = 0

# Mark Positions
while current_increment <= 500000:
    if positions[current_position_index]:
        positions[current_position_index] = False
    current_increment += 1
    current_position_index = (current_position_index + current_increment) % size

# Check Status of Positions
unmarked_positions = [pos for pos in positions if pos]

# Output Result
if len(unmarked_positions) == 0:
    print("YES")
else:
    print("NO")

# End
