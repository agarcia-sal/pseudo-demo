# Start the main process
# Step 2: Receive Input
firstSet = input()  # Read the first set of numbers as a string
secondSet = input()  # Read the second set of numbers as a string

# Step 3: Split Input into Lists
firstList = firstSet.split()  # Split the input string into a list of strings
secondList = secondSet.split()  # Split the second input string into a list of strings

# Step 4: Initialize a Counter
differenceCount = 0  # Initialize a counter to track the number of differing positions

# Step 5: Compare Corresponding Values
for index in range(3):  # Loop through indices 0 to 2
    valueFromFirst = int(firstList[index])  # Convert the value from the first list to an integer
    valueFromSecond = int(secondList[index])  # Convert the value from the second list to an integer
    
    # If the values differ, increment the difference count
    if valueFromFirst != valueFromSecond:
        differenceCount += 1

# Step 6: Evaluate the Result
if differenceCount < 3:  # Check if the number of differences is less than 3
    print("YES")  # Print YES if they differ in less than three positions
else:
    print("NO")  # Print NO if they differ in three or more positions

# End the main process
