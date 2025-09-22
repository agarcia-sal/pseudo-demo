# Step 1: Start the process.
# (No specific code needed here, just a comment)

# Step 2: Retrieve a number called totalNumbers from the user input.
totalNumbers = int(input())

# Step 3: Create a list named isAvailable with totalNumbers elements, and initialize all elements to True.
isAvailable = [True] * totalNumbers

# Step 4: Initialize a variable currentIndex to 0.
currentIndex = 0

# Step 5: Initialize a variable increment to 1.
increment = 1

# Step 6: Begin a loop that continues as long as increment is less than or equal to 500,000.
while increment <= 500000:
    # Check if the current position in isAvailable is True.
    if isAvailable[currentIndex]:  # isAvailable[currentIndex] is "True"
        isAvailable[currentIndex] = False  # Set that position to False.
    
    # Increment the increment variable by 1.
    increment += 1

    # Update currentIndex to point to the next position.
    currentIndex = (currentIndex + increment) % totalNumbers  # Wrap around using modulus.

# Step 7: Create a new list named availableItems with True values remaining in isAvailable.
availableItems = [item for item in isAvailable if item]

# Step 8: Check if the length of availableItems is 0.
if len(availableItems) == 0:
    # Step 8a: Output "YES" if all items are marked as unavailable.
    print("YES")
else:
    # Step 8b: Output "NO" if there are still available items.
    print("NO")

# Step 9: End the process.
# (No specific code needed here, just a comment)
