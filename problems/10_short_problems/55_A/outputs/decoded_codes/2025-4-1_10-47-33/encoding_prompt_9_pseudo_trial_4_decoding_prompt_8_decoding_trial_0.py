# Read Input
n = int(input())

# Initialize List
marked = [True] * n

# Initialize Counters
current_index = 0
step_size = 1

# Iterative Marking
while step_size <= 500000:
    if marked[current_index]:
        marked[current_index] = False
    step_size += 1
    current_index = (current_index + step_size) % n

# Check Marks
remaining_true = [mark for mark in marked if mark]

# Output Result
if len(remaining_true) == 0:
    print("YES")
else:
    print("NO")
