# Start the program.

# Prompt the user for input
userInput1 = input()  # Get the first set of values from the user
userInput2 = input()  # Get the second set of values from the user

# Split the input strings into individual components
valueList1 = userInput1.split()  # Break userInput1 into a list of values
valueList2 = userInput2.split()  # Break userInput2 into a list of values

# Initialize a counter for differences
differenceCounter = 0  # Set the counter to zero

# Compare the corresponding values from both lists
for index in range(3):  # Loop through indices 0 to 2
    valueA = int(valueList1[index])  # Convert value from the first list to an integer
    valueB = int(valueList2[index])  # Convert value from the second list to an integer

    # Check if the values are different
    if valueA != valueB:  # If they are not equal
        differenceCounter += 1  # Increment the counter

# Evaluate the total differences
if differenceCounter < 3:  # If less than 3 differences
    print("YES")  # Output "YES"
else:  # If 3 or more differences
    print("NO")  # Output "NO"

# End the program.
