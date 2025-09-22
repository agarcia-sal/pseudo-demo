# Start of the program

# Step 2: Input the integer number n
n = int(input())

# Step 3: Initialize the status list with n elements set to True
status = [True] * n

# Step 4: Set Counter
currentStep = 1
index = 0

# Step 5: Loop while currentStep is less than or equal to 500000
while currentStep <= 500000:
    # Check Status
    if status[index]:
        # Set the element at index to False
        status[index] = False
    
    # Increment Steps
    currentStep += 1
    
    # Update Index
    index = (index + currentStep) % n

# Step 6: Filter Active Status
activeElements = [element for element in status if element]

# Step 7: Check Result
if len(activeElements) == 0:
    print("YES")
else:
    print("NO")

# End of the program
