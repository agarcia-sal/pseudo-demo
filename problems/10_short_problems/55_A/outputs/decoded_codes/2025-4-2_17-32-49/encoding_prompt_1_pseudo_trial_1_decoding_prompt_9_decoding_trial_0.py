# Start

# Step 1: Read an integer n from user input
n = int(input())

# Step 2: Create a list isNotDeleted of size n with all elements set to True
isNotDeleted = [True] * n

# Step 3: Initialize the current index and i
currentIndex = 0
i = 1

# Step 4: Loop while i is less than or equal to 500000
while i <= 500000:
    # Check if the current index position is True
    if isNotDeleted[currentIndex]:
        # Mark the position as deleted (set to False)
        isNotDeleted[currentIndex] = False
    
    # Increment i by 1
    i += 1
    # Update currentIndex to be (currentIndex + i) modulo n
    currentIndex = (currentIndex + i) % n

# Step 5: Create a new list remainingTrue containing all True values from isNotDeleted
remainingTrue = [value for value in isNotDeleted if value]

# Step 6: Check the length of remainingTrue for output
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')

# End
