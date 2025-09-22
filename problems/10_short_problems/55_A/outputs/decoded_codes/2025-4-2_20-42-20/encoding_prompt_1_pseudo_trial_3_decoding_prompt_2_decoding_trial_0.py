# Step 1: Read an integer value n
n = int(input())

# Step 2: Initialize the data structures and variables
isTrue = [True] * n  # Create a list of size n filled with True values
currentIndex = 0
step = 1

# Step 3: Loop until step exceeds 500,000
while step <= 500000:
    if isTrue[currentIndex]:  # Check if the position is True
        isTrue[currentIndex] = False  # Set that position to False
    step += 1  # Increment step by 1
    currentIndex = (currentIndex + step) % n  # Update currentIndex

# Step 4: Filter remaining True values
remainingTrue = [value for value in isTrue if value]

# Step 5: Check outcome
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
