# 1. Start Program (No direct translation needed)

# 2. Accept Input
size = int(input())  # Take integer input from the user

# 3. Initialize Array
status = [True] * size  # Create a boolean array of length 'size' filled with True

# 4. Set Initial Variables
index = 0
increment = 1

# 5. Loop until a condition is met
while increment <= 500000:
    # 1. Check Current Status
    if status[index]:  # If status[index] is True
        status[index] = False  # Set status[index] to False
    
    # 2. Update Values
    increment += 1  # Increment increment by 1
    index = (index + increment) % size  # Update index to be (index + increment) modulo size

# 6. Filter Active Status
active_status = [s for s in status if s]  # Create a new list of elements that are still True

# 7. Determine If Any True Elements Exist
if len(active_status) == 0:  # If length of active_status is 0
    print("YES")  # Print "YES"
else:
    print("NO")  # Otherwise print "NO"

# 8. End Program (No direct translation needed)
