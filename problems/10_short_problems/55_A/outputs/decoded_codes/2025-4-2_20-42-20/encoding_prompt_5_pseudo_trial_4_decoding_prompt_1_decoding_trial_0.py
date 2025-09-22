# 1. Initialize the Variables:
n = int(input())  # Read an integer value representing the size of the list (n)
status = [True] * n  # Create a list called "status" with "True" values
current_position = 0  # Initialize "current_position" to 0
increment = 1  # Initialize "increment" to 1

# 2. Start the Elimination Process:
while increment <= 500000:  # While the "increment" is less than or equal to 500,000
    if status[current_position]:  # Check if the status at "current_position" is "True"
        status[current_position] = False  # Set the status at "current_position" to "False"
        
    increment += 1  # Increment "increment" by 1
    current_position = (current_position + increment) % n  # Update "current_position"

# 3. Check the Remaining Active Positions:
active_positions = [pos for pos in status if pos]  # Create a new list of active positions
if len(active_positions) == 0:  # If the length of "active_positions" is 0
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"
