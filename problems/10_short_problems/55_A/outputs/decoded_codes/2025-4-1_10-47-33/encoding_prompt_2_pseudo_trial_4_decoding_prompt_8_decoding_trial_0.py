# Step 1: Start

# Step 2: Input
n = int(input())

# Step 3: Initialize
is_available = [True] * n
current_position = 0
increment = 1

# Step 4: Processing Loop
while increment <= 500000:
    if is_available[current_position]:
        is_available[current_position] = False
    increment += 1
    current_position = (current_position + increment) % n

# Step 5: Identify Unavailable Positions
available_positions = [i for i in is_available if i]

# Step 6: Output
if len(available_positions) == 0:
    print("YES")
else:
    print("NO")

# Step 7: End
