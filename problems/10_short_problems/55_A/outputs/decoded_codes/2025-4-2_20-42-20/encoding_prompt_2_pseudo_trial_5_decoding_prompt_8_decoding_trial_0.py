# Step 1: Read the integer input
totalCount = int(input())

# Step 2: Create the boolean array initialized to True
booleanArray = [True] * totalCount

# Step 3: Initialize variables
incrementValue = 1
index = 0

# Step 4: Begin the loop
while incrementValue <= 500000:
    if booleanArray[index]:
        booleanArray[index] = False
    
    incrementValue += 1
    index = (index + incrementValue) % totalCount

# Step 5: Create a new list containing True values' positions
trueValues = [i for i in range(totalCount) if booleanArray[i]]

# Step 6: Check the size of trueValues and print result
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")
