# Step 1: Initialize Input
n = int(input())

# Step 2: Create a Boolean List
isActive = [True] * n

# Step 3: Set Up Variables
index = 0
counter = 1

# Step 4: Iterate While Counter is Less Than or Equal To 500000
while counter <= 500000:
    if isActive[index]:
        isActive[index] = False
    counter += 1
    index = (index + counter) % n

# Step 5: Filter Active Elements
activeElements = [active for active in isActive if active]

# Step 6: Check Active Elements
if len(activeElements) == 0:
    print("YES")
else:
    print("NO")
