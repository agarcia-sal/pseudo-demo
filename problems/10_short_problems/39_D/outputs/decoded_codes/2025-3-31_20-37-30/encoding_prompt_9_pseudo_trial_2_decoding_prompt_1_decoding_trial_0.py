# Start Program

# Receive Input
firstSet = input()
secondSet = input()

# Split Input Strings into Lists
numbersSet1 = firstSet.split()
numbersSet2 = secondSet.split()

# Initialize a Counter
differenceCount = 0

# Compare Each Position
for index in range(3):  # Loop through indices 0 to 2
    num1 = int(numbersSet1[index])
    num2 = int(numbersSet2[index])
    if num1 != num2:
        differenceCount += 1

# Output the Result
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program
