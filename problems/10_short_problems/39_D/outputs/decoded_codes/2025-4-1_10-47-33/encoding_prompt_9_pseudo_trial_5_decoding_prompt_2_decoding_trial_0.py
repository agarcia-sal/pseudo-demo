# Start the program

# Receive two input strings
firstSet = input()
secondSet = input()

# Split both input strings into lists
numbersFirst = firstSet.split()
numbersSecond = secondSet.split()

# Initialize a counter for differences
differenceCount = 0

# Loop through each number in both lists
for index in range(3):  # Loop from 0 to 2
    # Convert the number from both sets to integers
    numFirst = int(numbersFirst[index])
    numSecond = int(numbersSecond[index])
    
    # Check for differences
    if numFirst != numSecond:
        differenceCount += 1

# Evaluate the number of differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End of the program
