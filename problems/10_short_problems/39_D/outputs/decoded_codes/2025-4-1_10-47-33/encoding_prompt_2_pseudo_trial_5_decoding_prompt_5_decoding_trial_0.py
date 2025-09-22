# Start the program

# Prompt the user for input
userInput1 = input()  # Get the first set of values from the user
userInput2 = input()  # Get the second set of values from the user

# Split the input strings into individual components
valueList1 = userInput1.split()  # Break userInput1 into a list of values
valueList2 = userInput2.split()  # Break userInput2 into a list of values

# Initialize a counter for differences
differenceCounter = 0  # Set the counter to zero

# Compare the corresponding values from both lists
for index in range(3):  # Loop from index 0 to 2 inclusive
    # Convert values to integers
    valueA = int(valueList1[index])  # Convert value from the first list
    valueB = int(valueList2[index])  # Convert value from the second list
    
    # Check if values are different
    if valueA != valueB:
        differenceCounter += 1  # Increment the counter if they differ

# Evaluate the total differences
if differenceCounter < 3:
    print("YES")  # Output if differences are less than 3
else:
    print("NO")  # Output if differences are 3 or more

# End the program
