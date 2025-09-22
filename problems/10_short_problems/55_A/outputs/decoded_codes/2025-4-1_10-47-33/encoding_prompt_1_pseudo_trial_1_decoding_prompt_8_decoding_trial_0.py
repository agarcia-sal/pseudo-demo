# Step 1: Initialize the variable numberOfElements as the user input converted to an integer.
numberOfElements = int(input())

# Step 2: Create a list isIncluded of boolean values, each entry set to True
isIncluded = [True] * numberOfElements

# Step 3: Set the variable currentIndex to 0
currentIndex = 0

# Step 4: Set the variable increment to 1
increment = 1

# Step 5: While increment is less than or equal to 500000
while increment <= 500000:
    # If the value at isIncluded[currentIndex] is True, then set it to False
    if isIncluded[currentIndex]:
        isIncluded[currentIndex] = False
    # Increment increment by 1
    increment += 1
    # Update currentIndex to the new position
    currentIndex = (currentIndex + increment) % numberOfElements

# Step 6: Create a list trueValues by filtering isIncluded for values that are still True
trueValues = [value for value in isIncluded if value]

# Step 7: If the length of trueValues is equal to 0, output "YES", else output "NO"
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")
