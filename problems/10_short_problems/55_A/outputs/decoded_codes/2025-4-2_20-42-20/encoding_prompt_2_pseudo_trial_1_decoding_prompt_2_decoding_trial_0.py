# Start the program
# Get an integer input from the user
numberOfElements = int(input())

# Create a list `isAvailable` with `numberOfElements` elements initialized to True
isAvailable = [True] * numberOfElements

# Initialize variables
index = 0
increment = 1

# While increment is less than or equal to 500000
while increment <= 500000:
    # Check if the element at isAvailable[index] is True
    if isAvailable[index] == True:
        # If it is True, set isAvailable[index] to False
        isAvailable[index] = False
    
    # Increase increment by 1
    increment += 1
    
    # Update index to be (index + increment) mod numberOfElements
    index = (index + increment) % numberOfElements

# Create a new list `remainingTrue` that includes all elements in isAvailable that are still True
remainingTrue = [x for x in isAvailable if x]

# If the length of remainingTrue is equal to 0
if len(remainingTrue) == 0:
    # Output 'YES'
    print('YES')
else:
    # Otherwise, output 'NO'
    print('NO')
# End the program
