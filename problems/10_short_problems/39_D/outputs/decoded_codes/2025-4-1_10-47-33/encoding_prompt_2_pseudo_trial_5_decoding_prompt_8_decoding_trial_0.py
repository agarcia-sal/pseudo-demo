# Start the program.

# Prompt the user for input
userInput1 = input()
userInput2 = input()

# Split the input strings into individual components
valueList1 = userInput1.split()
valueList2 = userInput2.split()

# Initialize a counter for differences
differenceCounter = 0

# Compare the corresponding values from both lists
for index in range(3):
    valueA = int(valueList1[index])
    valueB = int(valueList2[index])
    if valueA != valueB:
        differenceCounter += 1

# Evaluate the total differences
if differenceCounter < 3:
    print("YES")
else:
    print("NO")

# End the program.
