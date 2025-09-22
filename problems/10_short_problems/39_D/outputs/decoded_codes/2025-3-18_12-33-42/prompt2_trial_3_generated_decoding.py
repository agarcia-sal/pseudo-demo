# Start the program

# Input Phase: Read the first and second line of input
firstInput = input()
secondInput = input()

# Processing Phase: Split the inputs into lists
firstValues = firstInput.split()
secondValues = secondInput.split()
differenceCount = 0  # Initialize the difference counter

# Comparison Phase: Compare the values in both lists
for i in range(3):  # Loop from 0 to 2 (three iterations)
    valueFromFirst = int(firstValues[i])  # Convert to integer
    valueFromSecond = int(secondValues[i])  # Convert to integer
    
    if valueFromFirst != valueFromSecond:  # Check for differences
        differenceCount += 1  # Increment the difference counter

# Decision Phase: Output based on the count of differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the program
