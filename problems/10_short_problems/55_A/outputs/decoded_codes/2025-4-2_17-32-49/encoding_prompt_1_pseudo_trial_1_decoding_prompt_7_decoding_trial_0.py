# Start of the program

# Step 1: Read an integer 'n' from user input
n = int(input())  # Getting the size for the list

# Step 2: Initialize a list 'isNotDeleted' of size 'n' with all elements set to True
isNotDeleted = [True] * n  # List initialized with True values

# Step 3: Set initial variables
currentIndex = 0  # Current index initialized to 0
i = 1  # Variable 'i' initialized to 1

# Step 4: Loop through a range while 'i' is less than or equal to 500000
while i <= 500000:
    # Check the condition of the current index
    if isNotDeleted[currentIndex]:
        isNotDeleted[currentIndex] = False  # Mark as deleted

    # Increment 'i' by 1
    i += 1

    # Update 'currentIndex' to be (currentIndex + i) modulo n
    currentIndex = (currentIndex + i) % n

# Step 5: Create a new list 'remainingTrue' containing all elements that are still True
remainingTrue = [value for value in isNotDeleted if value]  # Collecting remaining True values

# Step 6: Determine output based on remaining values
if len(remainingTrue) == 0:  # Check if there are no remaining True values
    print('YES')  # All elements marked as deleted
else:
    print('NO')  # There are still some True elements

# End of the program
