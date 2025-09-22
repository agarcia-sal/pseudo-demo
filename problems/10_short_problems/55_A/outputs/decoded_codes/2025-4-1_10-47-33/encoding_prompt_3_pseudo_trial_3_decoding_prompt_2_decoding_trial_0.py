# Input
n = int(input())  # Get an integer value 'n' from user input

# Initialize a boolean list 'isActive' of size n
isActive = [True] * n  # Set isActive to a list of size n filled with True
index = 0
increment = 1

# Process to modify the 'isActive' list
while increment <= 500000:
    if isActive[index]:  # If isActive at index is True
        isActive[index] = False  # Mark isActive at index as False
    # Update increment and index for the next iteration
    increment += 1  # Increment increment by 1
    index = (index + increment) % n  # Update index to (index + increment) modulo n

# Create a new list 'activeElements' from the 'isActive' list
activeElements = [x for x in isActive if x]  # Set activeElements to a list containing all True values from isActive

# Output Result
if len(activeElements) == 0:  # If the size of activeElements is 0
    print('YES')  # Indicating all elements are marked False
else:
    print('NO')  # Indicating there are still True elements present
