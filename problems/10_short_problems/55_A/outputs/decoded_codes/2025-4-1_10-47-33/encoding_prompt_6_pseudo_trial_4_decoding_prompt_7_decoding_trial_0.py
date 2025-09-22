# Begin the program execution

# Step 1: Read an integer input n
numberOfElements = int(input())

# Step 2: Create a list 'isActive' of boolean values, initially all set to True
isActive = [True] * numberOfElements

# Step 3: Initialize the index variables
currentIndex = 0
increment = 1

# Step 4: Loop until increment reaches or exceeds 500000
while increment <= 500000:
    
    # Step 5: If the current position in 'isActive' is True
    if isActive[currentIndex]:
        # Step 6: Set the current position in 'isActive' to False
        isActive[currentIndex] = False
    
    # Step 7: Increment the 'increment' value
    increment += 1
    
    # Step 8: Update 'currentIndex' using modular arithmetic
    currentIndex = (currentIndex + increment) % numberOfElements

# Step 9: Create a new list 'activeElements' with True values from 'isActive'
activeElements = [i for i in isActive if i]

# Step 10: Check if 'activeElements' is empty
if len(activeElements) == 0:
    # Step 11: If empty, output 'YES'
    print('YES')
else:
    # Step 12: If not empty, output 'NO'
    print('NO')
