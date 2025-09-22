# Start the program.

# Step 2: Receive two input strings
firstSet = input()  # Represents a list of three numbers
secondSet = input()  # Represents a list of three numbers

# Step 3: Split both input strings into lists
numbersFirst = firstSet.split()  # Creates a list by dividing firstSet
numbersSecond = secondSet.split()  # Creates a list by dividing secondSet

# Step 4: Initialize a counter for differences
differenceCount = 0  # Set a variable to count differences

# Step 5: Loop through each number in both lists
for index in range(3):  # Loop from 0 to 2
    numFirst = int(numbersFirst[index])   # Convert the number from numbersFirst to an integer
    numSecond = int(numbersSecond[index])  # Convert the number from numbersSecond to an integer
    if numFirst != numSecond:  # If the numbers are not equal
        differenceCount += 1  # Increase the difference count by 1

# Step 6: Evaluate the number of differences
if differenceCount < 3:  # If differences are less than 3
    print("YES")  # Print YES
else:  # Otherwise
    print("NO")  # Print NO

# End of the program.
