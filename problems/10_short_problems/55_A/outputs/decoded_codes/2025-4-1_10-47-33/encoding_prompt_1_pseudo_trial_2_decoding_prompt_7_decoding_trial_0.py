# Initialize Input
n = int(input())  # Read an integer n representing the size of the list

# Create a Boolean List
isActive = [True] * n  # Initialize a list of size n where all elements are set to True

# Set Up Variables
index = 0  # Initialize the index
counter = 1  # Initialize the counter

# Iterate While Counter is Less Than or Equal To 500000
while counter <= 500000:
    if isActive[index]:  # Check if the current index is active
        isActive[index] = False  # Set that position to False indicating it's no longer active
    
    counter += 1  # Increment the counter
    index = (index + counter) % n  # Update index, wrapping around using modulo

# Filter Active Elements
activeElements = [i for i in range(n) if isActive[i]]  # List comprehension to get active indices

# Check Active Elements
if len(activeElements) == 0:  # If no active elements left
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"
