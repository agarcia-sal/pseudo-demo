# Step 1: Start
# Step 2: Read an integer 'n' from user input
n = int(input())

# Step 3: Initialize a list 'positions' of size 'n' with all elements set to True
positions = [True] * n

# Step 4: Set a variable 'currentIndex' to 0
currentIndex = 0

# Step 5: Set a variable 'stepSize' to 1
stepSize = 1

# Step 6: While 'stepSize' is less than or equal to 500000
while stepSize <= 500000:
    # Step 6a: If positions[currentIndex] is True
    if positions[currentIndex] == True:
        # Step 6ai: Mark positions[currentIndex] as False
        positions[currentIndex] = False
        
    # Step 6b: Increase 'stepSize' by 1
    stepSize += 1
    
    # Step 6c: Update 'currentIndex' to (currentIndex + stepSize) modulo 'n'
    currentIndex = (currentIndex + stepSize) % n

# Step 7: Create a new list 'remainingTruePositions' containing all elements from 'positions' that are still True
remainingTruePositions = [pos for pos in positions if pos]

# Step 8: If remainingTruePositions is empty
if not remainingTruePositions:
    # Step 8a: Print "YES" (indicating that all positions are False)
    print("YES")
# Step 9: Else
else:
    # Step 9a: Print "NO" (indicating that there are still True positions)
    print("NO")

# Step 10: End
