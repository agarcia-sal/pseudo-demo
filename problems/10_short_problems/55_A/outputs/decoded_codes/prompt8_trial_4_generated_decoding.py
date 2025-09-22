# Initialize
n = int(input())
isMarked = [True] * n

# Set Up Iteration Variables
index = 0
counter = 1

# Iterate While Counter is Less Than or Equal to 500,000
while counter <= 500000:
    if isMarked[index]:
        isMarked[index] = False  # mark this index as processed
    counter += 1
    index = (index + counter) % n  # wrap around if necessary

# Check Remaining Unmarked Elements
remainingTrue = [item for item in isMarked if item]

# Output Results
if not remainingTrue:
    print("YES")
else:
    print("NO")


def process_indices(n):
    isMarked = [True] * n
    index = 0
    counter = 1
    while counter <= 500000:
        if isMarked[index]:
            isMarked[index] = False
        counter += 1
        index = (index + counter) % n
    return "YES" if not any(isMarked) else "NO"
