# Step 1: Input
n = int(input())

# Step 2: Initialize
isTrue = [True] * n  # A boolean array of size n, all set to True

# Step 3: Set initial variables
currentIndex = 0
increment = 1

# Step 4: Loop
while increment <= 500000:
    if isTrue[currentIndex]:  # Check if the current index is True
        isTrue[currentIndex] = False  # Mark it as processed
        
    increment += 1  # Increment the increment variable
    currentIndex = (currentIndex + increment) % n  # Update currentIndex with wrapping

# Step 5: Check results
remainingTrue = [value for value in isTrue if value]  # Create a list of remaining True values

# Step 6: Output
if len(remainingTrue) == 0:  # If no True values remain
    print("YES")  # All elements were processed
else:
    print("NO")  # There are elements that remain True
