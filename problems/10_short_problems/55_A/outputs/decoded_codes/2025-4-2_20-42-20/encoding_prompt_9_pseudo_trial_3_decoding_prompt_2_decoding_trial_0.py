# 1. Start Program

# 2. Accept Input:
size = int(input())  # Set size to the integer value received from user input.

# 3. Initialize Array:
status = [True] * size  # Create a boolean array of length size and fill it with True.

# 4. Set Initial Variables:
index = 0  # Set index to 0.
increment = 1  # Set increment to 1.

# 5. Loop until a condition is met:
while increment <= 500000:  # While increment is less than or equal to 500,000 do the following:
    # 1. Check Current Status:
    if status[index]:  # If status[index] is True, then:
        status[index] = False  # Set status[index] to False.
    
    # 2. Update Values:
    increment += 1  # Increment increment by 1.
    index = (index + increment) % size  # Update index to be (index + increment) modulo size.

# 6. Filter Active Status:
active_status = [s for s in status if s]  # Create a list of all True elements in status.

# 7. Determine If Any True Elements Exist:
if len(active_status) == 0:  # If the length of active_status is 0, then:
    print("YES")  # Print "YES".
else:  # Otherwise:
    print("NO")  # Print "NO".

# 8. End Program
