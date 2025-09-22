# Start the main process
# Step 1: Read a line of input from the user for the first input string
inputString1 = input()

# Step 2: Read another line of input from the user for the second input string
inputString2 = input()

# Step 3: Split the first input string into a list of strings called tokens1
tokens1 = inputString1.split()

# Step 4: Split the second input string into a list of strings called tokens2
tokens2 = inputString2.split()

# Step 5: Initialize a counter variable differenceCount to track differences
differenceCount = 0

# Step 6: Iterate over the first three entries of both lists
for i in range(3):
    # Convert current entry in tokens1 to an integer
    valueFromFirstInput = int(tokens1[i])
    # Convert current entry in tokens2 to an integer
    valueFromSecondInput = int(tokens2[i])
    
    # Step 7: Check if the values from both inputs are different
    if valueFromFirstInput != valueFromSecondInput:
        differenceCount += 1  # Increment the count if they are different

# Step 8: After checking all three entries, determine the outcome
if differenceCount < 3:
    # Output "YES" if there are fewer than three differences
    print("YES")
else:
    # Output "NO" if there are three or more differences
    print("NO")

# End of the process
