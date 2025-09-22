# Start the main process
# Read a line of input from the user and store it in the variable inputString1
inputString1 = input()
# Read another line of input from the user and store it in the variable inputString2
inputString2 = input()

# Split inputString1 into a list of strings called tokens1
tokens1 = inputString1.split()
# Split inputString2 into a list of strings called tokens2
tokens2 = inputString2.split()

# Initialize a counter variable differenceCount to zero
differenceCount = 0

# For each index from 0 to 2 (representing the first three entries of both lists)
for index in range(3):
    # Convert the current entry in tokens1 to an integer
    valueFromFirstInput = int(tokens1[index])
    # Convert the current entry in tokens2 to an integer
    valueFromSecondInput = int(tokens2[index])
    
    # If valueFromFirstInput is not equal to valueFromSecondInput
    if valueFromFirstInput != valueFromSecondInput:
        # Increment differenceCount by one
        differenceCount += 1

# After checking all three entries, if differenceCount is less than 3
if differenceCount < 3:
    # Output "YES" to indicate that there are fewer than three differences
    print("YES")
else:
    # Otherwise, output "NO" to indicate that there are three or more differences
    print("NO")
