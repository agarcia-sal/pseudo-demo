# Begin the main process
# Step 2: Prompt for inputs
firstInput = input()  # Prompt the user to input the first set of values
secondInput = input()  # Prompt the user to input the second set of values
# Step 4: Split inputs into lists
firstValues = firstInput.split()  # Split the first input string into a list
secondValues = secondInput.split()  # Split the second input string into a list
# Step 6: Initialize counter
differenceCount = 0  # Initialize the counter to zero

# Step 7: Compare values
for index in range(3):  # Loop through indices 0 to 2
    firstValue = int(firstValues[index])  # Convert first value to int
    secondValue = int(secondValues[index])  # Convert second value to int
    if firstValue != secondValue:  # If values are not equal
        differenceCount += 1  # Increment the difference count

# Step 8: Output decision based on difference count
if differenceCount < 3:  # Check if the difference count is less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End the main process
