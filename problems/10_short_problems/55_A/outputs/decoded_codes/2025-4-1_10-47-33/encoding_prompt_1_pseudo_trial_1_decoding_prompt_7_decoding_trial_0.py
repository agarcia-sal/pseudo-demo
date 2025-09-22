# Step 1: Initialize the variable `numberOfElements` as user input converted to integer
numberOfElements = int(input())

# Step 2: Create a list `isIncluded` of boolean values, all set to True
isIncluded = [True] * numberOfElements

# Step 3: Set the variable `currentIndex` to 0
currentIndex = 0

# Step 4: Set the variable `increment` to 1
increment = 1

# Step 5: Loop while `increment` is less than or equal to 500000
while increment <= 500000:
    # - If `isIncluded[currentIndex]` is True, set it to False
    if isIncluded[currentIndex]:
        isIncluded[currentIndex] = False
    
    # - Increment `increment` by 1
    increment += 1
    
    # - Update `currentIndex` using the modulo operation
    currentIndex = (currentIndex + increment) % numberOfElements

# Step 6: Create a list of `trueValues` containing indices that are still included
trueValues = [value for value in isIncluded if value]

# Step 7: Check if any indices are still True and output the result
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")
