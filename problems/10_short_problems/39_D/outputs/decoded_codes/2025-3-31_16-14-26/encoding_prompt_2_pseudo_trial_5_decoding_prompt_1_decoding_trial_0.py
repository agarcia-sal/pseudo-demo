# 1. Start the main process. (No direct translation needed)

# 2. Read a line of input from the user and store it in the variable `inputString1`.
inputString1 = input()

# 3. Read another line of input from the user and store it in the variable `inputString2`.
inputString2 = input()

# 4. Split `inputString1` into a list of strings called `tokens1`.
tokens1 = inputString1.split()

# 5. Split `inputString2` into a list of strings called `tokens2`.
tokens2 = inputString2.split()

# 6. Initialize a counter variable `differenceCount` to zero.
differenceCount = 0

# 7. For each index from 0 to 2:
for index in range(3):
    # Convert the current entry in `tokens1` to an integer.
    valueFromFirstInput = int(tokens1[index])
    # Convert the current entry in `tokens2` to an integer.
    valueFromSecondInput = int(tokens2[index])
    
    # If `valueFromFirstInput` is not equal to `valueFromSecondInput`, increment `differenceCount`.
    if valueFromFirstInput != valueFromSecondInput:
        differenceCount += 1

# 8. After checking all three entries, if `differenceCount` is less than 3:
if differenceCount < 3:
    # Output "YES".
    print("YES")
# 9. Otherwise:
else:
    # Output "NO".
    print("NO")

# 10. End the process. (No direct translation needed)
