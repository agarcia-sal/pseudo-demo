# Begin the program
# Step 2: Get an integer input from the user
totalElements = int(input())

# Step 3: Create a boolean list initialized to True
booleanList = [True] * totalElements

# Step 4: Initialize currentIndex and increment
currentIndex = 0
increment = 1

# Step 5: Loop that continues while increment is less than or equal to 500,000
while increment <= 500000:
    # Step 5a: Check if the current position in booleanList is True
    if booleanList[currentIndex]:
        # Step 5a.i: Set that position in booleanList to False
        booleanList[currentIndex] = False
    
    # Step 5b: Increase the value of increment by 1
    increment += 1
    
    # Step 5c: Update currentIndex and wrap around using modulo
    currentIndex = (currentIndex + increment) % totalElements

# Step 6: Create a new list for the remaining True values
remainingTrueValues = [value for value in booleanList if value]

# Step 7: Check the length of remainingTrueValues
if len(remainingTrueValues) == 0:
    # Step 7a: If length is 0, output "YES"
    print("YES")
else:
    # Step 7b: Otherwise, output "NO"
    print("NO")

# End the program
