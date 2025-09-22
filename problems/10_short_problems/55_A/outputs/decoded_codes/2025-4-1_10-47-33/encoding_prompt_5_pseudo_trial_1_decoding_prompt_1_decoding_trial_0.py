# 1. Start the program.
# (No action needed in Python, just start writing code)

# 2. Get a number 'n' from the user which indicates the size of the list.
n = int(input())

# 3. Initialize a list 'booleanList' with 'n' elements all set to TRUE.
booleanList = [True] * n  # Use True to represent TRUE

# 4. Set variable 'index' to 0.
index = 0

# 5. Set variable 'increment' to 1.
increment = 1

# 6. WHILE increment is less than or equal to 500000 DO:
while increment <= 500000:
    # 6a. IF booleanList at position 'index' is TRUE THEN:
    if booleanList[index] == True:
        # 6ai. Set booleanList at position 'index' to FALSE.
        booleanList[index] = False
        
    # 6b. Increase increment by 1.
    increment += 1
    
    # 6c. Update index to (index + increment) modulo n to wrap around if it exceeds n.
    index = (index + increment) % n

# 7. Create a new list 'remainingTrue' that contains all TRUE values from booleanList.
remainingTrue = [value for value in booleanList if value == True]

# 8. IF the length of remainingTrue is 0 THEN:
if len(remainingTrue) == 0:
    # 8a. PRINT "YES"
    print("YES")
# 9. ELSE:
else:
    # 9a. PRINT "NO"
    print("NO")

# 10. End the program.
# (No further action needed, the program ends after printing)
