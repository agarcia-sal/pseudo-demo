# Step 1: Initialize the variable numberOfElements as the user input converted to an integer
numberOfElements = int(input())

# Step 2: Create a list isIncluded of boolean values, initialized to True
isIncluded = [True] * numberOfElements

# Step 3: Set the variable currentIndex to 0
currentIndex = 0

# Step 4: Set the variable increment to 1
increment = 1

# Step 5: While increment is less than or equal to 500000
while increment <= 500000:
    # If the value at isIncluded[currentIndex] is True, set it to False
    if isIncluded[currentIndex]:
        isIncluded[currentIndex] = False
    
    # Increment increment by 1
    increment += 1
    
    # Update currentIndex
    currentIndex = (currentIndex + increment) % numberOfElements

# Step 6: Create a list trueValues by filtering the isIncluded list for values that are True
trueValues = [value for value in isIncluded if value]

# Step 7: Check the length of trueValues and output accordingly
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")
