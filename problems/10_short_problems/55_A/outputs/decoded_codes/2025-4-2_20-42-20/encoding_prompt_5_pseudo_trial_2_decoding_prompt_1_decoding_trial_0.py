# 1. Start Program (No code needed)

# 2. Retrieve Input:
n = int(input())  # Read an integer value n

# 3. Initialize List:
status = [True] * n  # Create a list called status with n elements, all set to True

# 4. Initialize Variables:
index = 0  # Set a variable index to 0
increment = 1  # Set a variable increment to 1

# 5. Perform Modifications:
while increment <= 500000:  # While increment is less than or equal to 500000
    if status[index]:  # If status[index] is True
        status[index] = False  # Set status[index] to False
    increment += 1  # Increase increment by 1
    index = (index + increment) % n  # Update index

# 6. Check Remaining Active Elements:
active_elements = [s for s in status if s]  # Create a list of all active (True) elements

# 7. Determine Output:
if len(active_elements) == 0:  # If the length of active_elements is 0
    print("YES")  # Print "YES"
else:  # Else
    print("NO")  # Print "NO"

# 8. End Program (No code needed)
