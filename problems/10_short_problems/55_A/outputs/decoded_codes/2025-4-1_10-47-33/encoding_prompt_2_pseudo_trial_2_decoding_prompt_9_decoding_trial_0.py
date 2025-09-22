# Begin the program
# Read an integer value n from user input
n = int(input())

# Create a list isActive of length n, where all elements are initially set to True
isActive = [True] * n

# Initialize a variable currentIndex to 0
currentIndex = 0

# Initialize a variable increment to 1
increment = 1

# While increment is less than or equal to 500000, do the following
while increment <= 500000:
    # If the element at currentIndex in the list isActive is True
    if isActive[currentIndex]:
        # Set the element at currentIndex in the list isActive to False
        isActive[currentIndex] = False
    
    # Increment increment by 1
    increment += 1
    
    # Update currentIndex to be the sum of currentIndex and increment,
    # then find the remainder when divided by n
    currentIndex = (currentIndex + increment) % n

# Create a list activeElements that contains only the elements from isActive that are still True
activeElements = [elem for elem in isActive if elem]

# If the length of activeElements is equal to 0
if len(activeElements) == 0:
    # Output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")
# End the program
