# 1. Initialize Input
n = int(input())

# 2. Create a Boolean List
isActive = [True] * n

# 3. Set Up Variables
index = 0
counter = 1

# 4. Iterate While Counter is Less Than or Equal To 500000
while counter <= 500000:
    if isActive[index]:
        isActive[index] = False
    counter += 1
    index = (index + counter) % n  # Update index with wrapping around

# 5. Filter Active Elements
activeElements = [active for active in isActive if active]

# 6. Check Active Elements
if len(activeElements) == 0:
    print("YES")
else:
    print("NO")
