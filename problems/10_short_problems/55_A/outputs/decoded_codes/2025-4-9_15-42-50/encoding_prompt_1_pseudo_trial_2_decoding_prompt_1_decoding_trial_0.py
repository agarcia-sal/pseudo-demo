# 1. Start
# 2. Read an integer 'n' from user input
n = int(input())

# 3. Initialize a list 'positions' of size 'n' with all elements set to True
positions = [True] * n

# 4. Set a variable 'cur' to 0
cur = 0

# 5. Set a variable 'stsiz' to 1
stsiz = 1

# 6. While 'stsiz' is less than or equal to 500000:
while stsiz <= 500000:
    # 6a. If positions[cur] is True:
    if positions[cur]:
        # 6a.i. Mark positions[cur] as False
        positions[cur] = False
    
    # 6b. Increase 'stsiz' by 1
    stsiz += 1
    
    # 6c. Update 'cur' to (cur + stsiz) modulo 'n'
    cur = (cur + stsiz) % n

# 7. Create a new list 'remtrpos' containing all elements from 'positions' that are still True
remtrpos = [pos for pos in positions if pos]

# 8. If remtrpos is empty:
if not remtrpos:
    # 8a. Print "YES" (indicating that all positions are False)
    print("YES")
# 9. Else:
else:
    # 9a. Print "NO" (indicating that there are still True positions)
    print("NO")

# 10. End
