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
for index in range(3):  # For each index from 0 to 2 (inclusive)
    valueA = int(valueList1[index])  # Convert to integer
    valueB = int(valueList2[index])  # Convert to integer
    if valueA != valueB:  # If they are not equal
        differenceCounter += 1  # Increment the counter

# Evaluate the total differences
if differenceCounter < 3:  # If less than 3 differences
    print("YES")  # Output "YES"
else:  # Otherwise
    print("NO")  # Output "NO"

# End the program.
