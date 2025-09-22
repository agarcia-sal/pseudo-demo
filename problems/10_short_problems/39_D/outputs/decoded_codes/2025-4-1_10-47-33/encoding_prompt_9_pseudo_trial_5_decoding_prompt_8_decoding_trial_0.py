# Start the program.

# Receive two input strings:
firstSet = input()
secondSet = input()

# Split both input strings into lists:
numbersFirst = firstSet.split()
numbersSecond = secondSet.split()

# Initialize a counter for differences:
differenceCount = 0

# Loop through each number in both lists:
for index in range(3):
    # Convert the number from numbersFirst and numbersSecond at the current index from string to an integer.
    if int(numbersFirst[index]) != int(numbersSecond[index]):
        # Increase differenceCount by 1.
        differenceCount += 1

# Evaluate the number of differences:
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End of the program.
