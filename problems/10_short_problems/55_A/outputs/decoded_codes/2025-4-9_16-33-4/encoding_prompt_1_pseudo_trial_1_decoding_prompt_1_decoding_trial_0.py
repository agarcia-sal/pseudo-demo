# 1. Start: Begin the program.

# 2. Read Input:
inp = input()  # Prompt the user for a number
siz = int(inp)  # Convert inp to an integer

# 3. Initialize Boolean List:
boo = [True] * siz  # Create a list with siz elements, all set to True

# 4. Initialize Index Variables:
cur = 0  # cur tracks the position in the list
stct = 1  # stct determines how many steps to skip

# 5. Loop:
while stct <= 500000:  # While stct is less than or equal to 500,000
    # Check Boolean Value:
    if boo[cur]:  # If boo[cur] is True
        boo[cur] = False  # Set boo[cur] to False
    
    stct += 1  # Increment stct by 1
    cur = (cur + stct) % siz  # Update cur with the new position

# 6. Filter Remaining True Values:
rem_tr = [value for value in boo if value]  # Create a list of remaining True values from boo

# 7. Check Remaining Elements:
if len(rem_tr) == 0:  # If the length of rem_tr is 0
    print("YES")  # Print "YES" (meaning all were marked False)
else:
    print("NO")  # Print "NO" (meaning some remain True)

# 8. End: Finish the program.
