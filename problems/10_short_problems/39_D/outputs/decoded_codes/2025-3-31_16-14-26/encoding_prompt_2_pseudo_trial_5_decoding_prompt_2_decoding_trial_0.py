# Start the main process
# Step 2: Read input from user
inputString1 = input()
inputString2 = input()

# Step 4: Split the input strings into lists
tokens1 = inputString1.split()
tokens2 = inputString2.split()

# Step 6: Initialize the difference counter
differenceCount = 0

# Step 7: Loop through the first three entries of both lists
for i in range(3):
    valueFromFirstInput = int(tokens1[i])  # Convert the entry to integer
    valueFromSecondInput = int(tokens2[i])  # Convert the entry to integer
    
    # Check for differences
    if valueFromFirstInput != valueFromSecondInput:
        differenceCount += 1  # Increment the counter if they are not equal

# Step 8: Output the result based on the difference count
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the process
