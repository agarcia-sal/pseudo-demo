# Start

# Input Requirement: Read an integer value denoting a size, referred to as totalElements.
totalElements = int(input())

# Initialize: Create a list named isActive with totalElements elements, all set to True.
isActive = [True] * totalElements  # List to track active status of elements
index = 0  # Variable to track the current position in the list
step = 1  # Variable to track the number of steps taken in each iteration

# Loop: Continue looping while the step variable is less than or equal to 500,000.
while step <= 500000:
    # Check if the element at the current index in the isActive list is still True
    if isActive[index]:  # If the current element is still active
        isActive[index] = False  # Mark that element as inactive
    
    step += 1  # Increase the step variable by 1 to move to the next step
    
    # Update the index: Addition of step and wrapping around using modulo
    index = (index + step) % totalElements

# Filter Active Elements: Create a new list named activeElements that includes only still True elements
activeElements = [i for i in isActive if i]  # This will hold active (True) elements

# Output Requirement: Check if the length of the activeElements list is equal to 0
if len(activeElements) == 0:
    print("YES")  # Indicating that all elements have been marked inactive
else:
    print("NO")   # Indicating that there are still active elements

# End
