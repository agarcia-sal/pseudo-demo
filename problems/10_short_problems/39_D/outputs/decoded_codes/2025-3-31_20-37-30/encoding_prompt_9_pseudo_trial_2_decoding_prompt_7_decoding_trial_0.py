# Start Program

# Receive Input
firstSet = input()  # Get the first set of numbers from the user
secondSet = input()  # Get the second set of numbers from the user

# Split Input Strings into Lists
numbersSet1 = firstSet.split()  # Convert firstSet into a list of strings
numbersSet2 = secondSet.split()  # Convert secondSet into a list of strings

# Initialize a Counter
differenceCount = 0  # Counter for differing positions

# Compare Each Position
for index in range(3):  # Iterate over the three positions
    num1 = int(numbersSet1[index])  # Convert to integer from numbersSet1
    num2 = int(numbersSet2[index])  # Convert to integer from numbersSet2
    if num1 != num2:  # Check if the numbers differ
        differenceCount += 1  # Increase the count if they differ

# Output the Result
if differenceCount < 3:  # Check if differences are less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End Program
