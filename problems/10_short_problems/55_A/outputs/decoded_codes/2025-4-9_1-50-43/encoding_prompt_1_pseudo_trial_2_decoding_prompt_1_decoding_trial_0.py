# Step 1: Initialize Input
n = int(input())  # Get a number n from user input

# Step 2: Create a List of Truth Values
truthList = [True] * n  # Create a list named truthList with n elements, all set to True

# Step 3: Set Up Indices and Loop Control
currentIndex = 0  # Initialize currentIndex to 0
step = 1  # Initialize step to 1

# Step 4: Loop
while step <= 500000:  # Repeat while step is less than or equal to 500,000
    if truthList[currentIndex]:  # Check if the value at currentIndex is True
        truthList[currentIndex] = False  # Set that value to False
    step += 1  # Increment step by 1
    currentIndex = (currentIndex + step) % n  # Update currentIndex

# Step 5: Check Remaining Truth Values
remainingTrueValues = [value for value in truthList if value]  # Filter the True values

# Step 6: Output Result
if not remainingTrueValues:  # Check if remainingTrueValues is empty
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"
