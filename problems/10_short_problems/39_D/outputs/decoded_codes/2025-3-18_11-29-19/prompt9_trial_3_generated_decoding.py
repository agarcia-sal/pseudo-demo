# Start Main Program

# Receive Input: 
firstSet = input()  # Read the first set of numbers from user input
secondSet = input()  # Read the second set of numbers from user input

# Split Input Strings into Lists:
firstList = firstSet.split()  # Convert firstSet into a list of strings
secondList = secondSet.split()  # Convert secondSet into a list of strings

# Initialize Difference Counter:
differenceCount = 0  # This will track how many positions have different values

# Compare Each Position:
for index in range(3):  # Loop over each of the three positions
    firstValue = int(firstList[index])  # Convert the value in firstList to an integer
    secondValue = int(secondList[index])  # Convert the value in secondList to an integer
    
    # If the values are not equal, increase the difference count
    if firstValue != secondValue:
        differenceCount += 1

# Determine Result:
if differenceCount < 3:  # Check if the count of differences is less than 3
    print("YES")  # Output "YES" if the condition is met
else:
    print("NO")  # Otherwise, output "NO"

# End Main Program
