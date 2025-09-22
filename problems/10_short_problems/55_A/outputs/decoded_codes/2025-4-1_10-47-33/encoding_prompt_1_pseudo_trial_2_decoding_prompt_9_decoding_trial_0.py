# Initialize Input
n = int(input())

# Create a Boolean List
isActive = [True] * n

# Set Up Variables
index = 0
counter = 1

# Iterate While Counter is Less Than or Equal To 500000
while counter <= 500000:
    if isActive[index]:
        isActive[index] = False
    counter += 1
    index = (index + counter) % n  # Wrap around if necessary

# Filter Active Elements
activeElements = [elem for elem in isActive if elem]

# Check Active Elements
if len(activeElements) == 0:
    print("YES")
else:
    print("NO")
