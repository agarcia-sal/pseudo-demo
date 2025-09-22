# Step 1: Read an integer n from the user
n = int(input())

# Step 2: Create a boolean array isTrue of size n, initialized to True
isTrue = [True] * n

# Step 3: Set initial variables
currentIndex = 0
increment = 1

# Step 4: Loop while increment is less than or equal to 500000
while increment <= 500000:
    # If isTrue[currentIndex] is True
    if isTrue[currentIndex]:
        # Mark it as processed
        isTrue[currentIndex] = False
    # Increment the increment variable
    increment += 1
    # Update currentIndex to be the sum of currentIndex and increment, modulo n
    currentIndex = (currentIndex + increment) % n

# Step 5: Create a list remainingTrue containing all elements of isTrue that are still True
remainingTrue = [x for x in isTrue if x]

# Step 6: Output the result
if len(remainingTrue) == 0:
    print("YES")  # All elements were processed
else:
    print("NO")   # There are elements that remain True
