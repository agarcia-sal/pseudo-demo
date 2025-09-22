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
for index in range(3):  # We are comparing three positions (0, 1, 2)
    num1 = int(numbersSet1[index])  # Convert the value from numbersSet1 to an integer
    num2 = int(numbersSet2[index])  # Convert the value from numbersSet2 to an integer
    
    if num1 != num2:  # Check if the numbers at the current position are different
        differenceCount += 1  # Increase differenceCount if they are not equal

# Output the Result
if differenceCount < 3:  # If the different positions are fewer than three
    print("YES")
else:
    print("NO")

# End Program
