# Start Program

# Get Input
n = int(input())

# Initialize List
booleanList = [True] * n

# Initialize Counters
index = 0
step = 1

# Loop through numbers
while step <= 500000:
    # Check Current Position
    if booleanList[index] == True:
        booleanList[index] = False  # Modify the position

    # Move to Next Step
    step += 1
    
    # Update Current Position
    index = (index + step) % n  # Circular movement

# Find Remaining Unchanged Positions
untouchedPositions = [value for value in booleanList if value == True]

# Check if Any Positions Remain Unchanged
if len(untouchedPositions) == 0:
    print("YES")  # All positions were modified
else:
    print("NO")   # Some positions remain unchanged

# End Program


def modify_positions(n, max_steps):
    booleanList = [True] * n
    index = 0
    step = 1
    
    while step <= max_steps:
        if booleanList[index]:
            booleanList[index] = False
        
        step += 1
        index = (index + step) % n
        
    return booleanList

# Main execution
n = int(input())
booleanList = modify_positions(n, 500000)
print("YES" if all(not value for value in booleanList) else "NO")
