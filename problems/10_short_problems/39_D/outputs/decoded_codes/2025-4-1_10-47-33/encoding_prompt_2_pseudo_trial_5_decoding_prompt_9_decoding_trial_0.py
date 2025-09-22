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
for index in range(3):  # Loop through indexes 0 to 2
    valueA = int(valueList1[index])  # Convert string to integer
    valueB = int(valueList2[index])  # Convert string to integer
    if valueA != valueB:  # Check if the values are different
        differenceCounter += 1  # Increment the counter if they differ

# Evaluate the total differences
if differenceCounter < 3:
    print("YES")  # Output "YES" if differences are less than 3
else:
    print("NO")  # Output "NO" if differences are 3 or more

# End the program.
