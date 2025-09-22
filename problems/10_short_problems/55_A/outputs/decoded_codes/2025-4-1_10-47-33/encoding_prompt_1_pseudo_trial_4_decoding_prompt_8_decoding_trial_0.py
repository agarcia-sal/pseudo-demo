# Step 1: Input
n = int(input())

# Step 2: Initialize
isTrue = [True] * n

# Step 3: Set initial variables
currentIndex = 0
increment = 1

# Step 4: Loop
while increment <= 500000:
    if isTrue[currentIndex]:
        isTrue[currentIndex] = False  # Mark it as processed
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Wrap around if necessary

# Step 5: Check results
remainingTrue = [value for value in isTrue if value]

# Step 6: Output
if len(remainingTrue) == 0:
    print("YES")  # All elements were processed
else:
    print("NO")  # Some elements remain True
