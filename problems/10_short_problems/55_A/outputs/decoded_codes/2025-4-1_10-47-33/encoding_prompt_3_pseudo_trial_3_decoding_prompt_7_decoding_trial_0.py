# Input: Get an integer value 'n' from user input
n = int(input())

# Initialize a boolean list 'isActive' of size n
isActive = [True] * n  # Create a list filled with True values
index = 0              # Starting index
increment = 1          # Starting increment

# Process to modify the 'isActive' list
while increment <= 500000:
    if isActive[index]:  # Check if the current index is still active
        isActive[index] = False  # Mark the current index as inactive

    # Update increment and index for the next iteration
    increment += 1  # Increment the increment value
    index = (index + increment) % n  # Calculate the next index, wrapping around with modulo

# Create a new list 'activeElements' from the 'isActive' list
activeElements = [value for value in isActive if value]  # Filter out all True values

# Output Result
if len(activeElements) == 0:  # Check if there are no active elements
    print('YES')  # Indicating all elements are marked False
else:
    print('NO')   # Indicating there are still True elements present
