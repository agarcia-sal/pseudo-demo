# Step 1: Input an integer to determine the size of the array
n = int(input())  # Read the size of the array from user input

# Step 2: Initialize a boolean array to track processed indexes
isTrue = [True] * n  # Create an array of size n, initialized to True

# Step 3: Set initial variables
currentIndex = 0  # Starting index
increment = 1     # Starting increment

# Step 4: Loop while increment is less than or equal to 500000
while increment <= 500000:
    # Check if the current index is still True
    if isTrue[currentIndex]:
        isTrue[currentIndex] = False  # Mark as processed
    
    increment += 1  # Increment the counter
    currentIndex = (currentIndex + increment) % n  # Update the index, wrapping around using modulus

# Step 5: Check results and create a list for remaining True elements
remainingTrue = [x for x in isTrue if x]  # List of elements that are still True

# Step 6: Output the final result
if len(remainingTrue) == 0:
    print("YES")  # All elements were processed
else:
    print("NO")   # Some elements are still True
