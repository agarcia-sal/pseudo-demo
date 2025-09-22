# Step 1: Start
# Step 2: Read an integer 'n' from user input
n = int(input())

# Step 3: Initialize a list 'positions' of size 'n' with all elements set to True
positions = [True] * n

# Step 4: Set a variable 'cur' to 0
cur = 0

# Step 5: Set a variable 'stsiz' to 1
stsiz = 1

# Step 6: While 'stsiz' is less than or equal to 500000:
while stsiz <= 500000:
    # Step 6a: If positions[cur] is True:
    if positions[cur]:
        # Step 6ai: Mark positions[cur] as False
        positions[cur] = False
    
    # Step 6b: Increase 'stsiz' by 1
    stsiz += 1
    
    # Step 6c: Update 'cur' to (cur + stsiz) modulo 'n'
    cur = (cur + stsiz) % n

# Step 7: Create a new list 'remtrpos' containing all elements from 'positions' that are still True
remtrpos = [pos for pos in positions if pos]

# Step 8: If remtrpos is empty:
if not remtrpos:
    # Step 8a: Print "YES"
    print("YES")
# Step 9: Else:
else:
    # Step 9a: Print "NO"
    print("NO")

# Step 10: End
