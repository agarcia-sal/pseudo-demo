# 1. Start

# 2. Input Requirement
totalElements = int(input())

# 3. Initialize
isActive = [True] * totalElements  # Create a list with totalElements, all set to True
index = 0  # Initialize the index to 0
step = 1   # Initialize the step to 1

# 4. Loop
while step <= 500000:  # Continue while step is less than or equal to 500,000
    if isActive[index]:  # Check if the current element is still True
        isActive[index] = False  # Mark it as inactive by setting it to False
    
    step += 1  # Increase the step variable by 1
    index = (index + step) % totalElements  # Update the index with wrapping

# 5. Filter Active Elements
activeElements = [e for e in isActive if e]  # Create a list of active elements

# 6. Output Requirement
if len(activeElements) == 0:  # Check if there are no active elements
    print("YES")  # All elements are inactive
else:
    print("NO")  # There are still active elements

# 7. End
