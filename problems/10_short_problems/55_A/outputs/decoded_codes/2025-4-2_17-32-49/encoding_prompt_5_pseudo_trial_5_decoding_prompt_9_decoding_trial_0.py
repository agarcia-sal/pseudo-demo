# Start program

# Input section
n = int(input())  # Prompt the user to enter a number and convert it to an integer

# Initialization
booleanList = [True] * n  # Create a list with n elements, all initialized to True
currentIndex = 0          # Set current index to 0
counter = 1               # Set counter to 1

# Loop for operations
while counter <= 500000:  # Continue looping while counter is less than or equal to 500000
    if booleanList[currentIndex]:  # Check if the current element is True
        booleanList[currentIndex] = False  # Change the current element to False
    
    counter += 1  # Increment the counter by 1
    currentIndex = (currentIndex + counter) % n  # Update the current index, wrapping around if necessary

# Check remaining True values
remainingTrue = [value for value in booleanList if value]  # Create a list of True elements in booleanList

if len(remainingTrue) == 0:  # Check if the length of remainingTrue is 0
    print("YES")  # All elements have been set to False
else:
    print("NO")   # Some elements are still True

# End program
