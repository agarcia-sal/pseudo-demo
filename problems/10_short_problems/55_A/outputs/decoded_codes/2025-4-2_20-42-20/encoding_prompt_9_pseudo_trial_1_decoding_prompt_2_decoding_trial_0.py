# Step 1: Read Input
n = int(input())

# Step 2: Initialize the Marking List
markings = [True] * n

# Step 3: Set Initial Variables
index = 0
step = 1

# Step 4: Start the Marking Process
while step <= 500000:
    if markings[index] == True:
        markings[index] = False  # Mark as processed
    step += 1
    index = (index + step) % n  # Circular index update

# Step 5: Check Remaining Marked Items
remainingTrue = [mark for mark in markings if mark == True]

# Step 6: Output Result
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
