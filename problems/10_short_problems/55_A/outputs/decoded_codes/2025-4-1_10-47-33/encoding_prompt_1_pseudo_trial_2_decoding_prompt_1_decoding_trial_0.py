# 1. Initialize Input
n = int(input())  # Read an integer n, which represents the size of the list.

# 2. Create a Boolean List
isActive = [True] * n  # Initialize a list isActive of size n with all elements set to True.

# 3. Set Up Variables
index = 0  # Set a variable index to 0.
counter = 1  # Set a variable counter to 1.

# 4. Iterate While Counter is Less Than or Equal To 500000
while counter <= 500000:  # While counter is less than or equal to 500000 do the following:
    if isActive[index]:  # If isActive at position index is True,
        isActive[index] = False  # set that position to False.
    counter += 1  # Increment the counter by 1.
    index = (index + counter) % n  # Update index to be (index + counter) modulo n.

# 5. Filter Active Elements
activeElements = [i for i in isActive if i]  # Create a new list activeElements containing only the elements in isActive that are still True.

# 6. Check Active Elements
if len(activeElements) == 0:  # If the length of activeElements is 0,
    print("YES")  # output "YES".
else:
    print("NO")  # Otherwise, output "NO".
