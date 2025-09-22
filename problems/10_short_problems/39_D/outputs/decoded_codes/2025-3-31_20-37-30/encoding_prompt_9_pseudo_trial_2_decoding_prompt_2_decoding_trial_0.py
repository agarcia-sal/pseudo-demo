# Start Program

# Receive Input
firstSet = input()
secondSet = input()

# Split Input Strings into Lists
numbersSet1 = firstSet.split()
numbersSet2 = secondSet.split()

# Initialize a Counter
differenceCount = 0  # This will track how many positions differ between the two sets

# Compare Each Position
for index in range(3):  # Iterating through indices 0, 1, 2
    num1 = int(numbersSet1[index])      # Convert the value from numbersSet1 to an integer
    num2 = int(numbersSet2[index])      # Convert the value from numbersSet2 to an integer
    if num1 != num2:                    # Check if the numbers differ
        differenceCount += 1             # Increase the differenceCount by 1 if they differ

# Output the Result
if differenceCount < 3:                # If the count of differences is less than 3
    print("YES")                       # Output "YES"
else:                                   # Otherwise
    print("NO")                        # Output "NO"

# End Program
