# Step 1: Start (Implicit in Python script)
# Step 2: Input
n = int(input())  # Read an integer number n from user input

# Step 3: Initialize
status = [True] * n  # Create a list called status with n elements, all set to True

# Step 4: Set Counter
currentStep = 1  # Initialize currentStep to 1
index = 0  # Initialize index to 0

# Step 5: Loop
while currentStep <= 500000:  # While currentStep is less than or equal to 500000
    # Step 5a: Check Status
    if status[index]:  # If the element at position index in status is True
        status[index] = False  # Set the element at index in status to False
    
    # Step 5b: Increment Steps
    currentStep += 1  # Increase currentStep by 1
    
    # Step 5c: Update Index
    index = (index + currentStep) % n  # Calculate next index

# Step 6: Filter Active Status
activeElements = [s for s in status if s]  # Create a new list activeElements that contains all True elements from status

# Step 7: Check Result
if len(activeElements) == 0:  # If the length of activeElements is 0
    print("YES")  # Print "YES"
else:  # Otherwise
    print("NO")  # Print "NO"

# Step 8: End (Implicit in Python script)
