# Start

# Input: Read an integer number `n` from user input
n = int(input())

# Initialize: Create a list called `status` with `n` elements, all set to `True`
status = [True] * n

# Set Counter: Initialize two variables, `currentStep` set to 1 and `index` set to 0
currentStep = 1
index = 0

# Loop: While `currentStep` is less than or equal to 500000
while currentStep <= 500000:
    # Check Status: If the element at position `index` in the `status` list is `True`
    if status[index]:
        # Set the element at `index` in `status` to `False`
        status[index] = False
    
    # Increment Steps: Increase `currentStep` by 1
    currentStep += 1
    
    # Update Index: Calculate the next index as `(index + currentStep) MOD n`
    index = (index + currentStep) % n

# Filter Active Status: Create a new list called `activeElements`
activeElements = [s for s in status if s]

# Check Result
if len(activeElements) == 0:
    print("YES")
else:
    print("NO")

# End
