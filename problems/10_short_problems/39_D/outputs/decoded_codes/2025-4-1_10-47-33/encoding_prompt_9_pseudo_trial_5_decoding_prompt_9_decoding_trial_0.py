# Start the program.

# Receive two input strings
firstSet = input()
secondSet = input()

# Split both input strings into lists
numbersFirst = firstSet.split()
numbersSecond = secondSet.split()

# Initialize a counter for differences
differenceCount = 0

# Loop through each number in both lists
for index in range(3):  # We know we are comparing exactly three numbers
    # Convert the number from each list from string to integer
    numberFirst = int(numbersFirst[index])
    numberSecond = int(numbersSecond[index])
    
    # If the numbers are not equal, increase the difference count
    if numberFirst != numberSecond:
        differenceCount += 1

# Evaluate the number of differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End of the program.
