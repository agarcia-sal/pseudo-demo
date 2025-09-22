# Start of the program

# Step 2: Read an integer number n from user input
n = int(input())

# Step 3: Initialize a list called status with n elements, all set to True
status = [True] * n

# Step 4: Initialize two variables
currentStep = 1
index = 0

# Step 5: Loop while currentStep is less than or equal to 500000
while currentStep <= 500000:
    # Step 5a: Check status
    if status[index]:  # If the element at position index in the status list is True
        status[index] = False  # Set the element at index in status to False

    # Step 5b: Increment steps
    currentStep += 1

    # Step 5c: Update index
    index = (index + currentStep) % n  # Calculate next index using modulo operation

# Step 6: Filter active status
activeElements = [s for s in status if s]  # Create a list of elements still set to True

# Step 7: Check result
if len(activeElements) == 0:  # If the length of activeElements is 0
    print("YES")  # Print "YES"
else:
    print("NO")  # Otherwise, print "NO"

# End of the program
