# Step 1: Input
n = int(input())  # Read an integer value n

# Step 2: Initialize
isTrue = [True] * n  # Create a list of size n filled with True
currentIndex = 0  # Initialize currentIndex to 0
step = 1  # Initialize step to 1

# Step 3: Loop until step exceeds 500,000
while step <= 500000:
    if isTrue[currentIndex]:  # Check if current position is True
        isTrue[currentIndex] = False  # Set that position in isTrue to False
    
    step += 1  # Increment step by 1
    currentIndex = (currentIndex + step) % n  # Update currentIndex

# Step 4: Filter
remainingTrue = [value for value in isTrue if value]  # Create a new list of remaining True values

# Step 5: Check outcome
if len(remainingTrue) == 0:  # If the length of remainingTrue is 0
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
