# Step 1: Read the integer input representing the number of elements.
n = int(input())

# Step 2: Initialize the data structures and variables.
# Create a list `isTrue` of size `n` filled with `True` values.
isTrue = [True] * n
# Initialize current index and step variables.
currentIndex = 0
step = 1

# Step 3: Loop until step exceeds 500,000.
while step <= 500000:
    # Check if isTrue at currentIndex is True.
    if isTrue[currentIndex]:
        # Set that position in isTrue to False.
        isTrue[currentIndex] = False
    
    # Increment step by 1.
    step += 1
    # Update currentIndex using the formula provided.
    currentIndex = (currentIndex + step) % n

# Step 4: Filter to create `remainingTrue` list consisting of all True values in isTrue.
remainingTrue = [value for value in isTrue if value]

# Step 5: Check the outcome.
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
