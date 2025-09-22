# Start the program.

# Receive two input strings
firstSet = input()  # First input string representing a list of three numbers
secondSet = input()  # Second input string representing a list of three numbers

# Split both input strings into lists
numbersFirst = firstSet.split()  # Create a list called numbersFirst
numbersSecond = secondSet.split()  # Create a list called numbersSecond

# Initialize a counter for differences
differenceCount = 0

# Loop through each number in both lists
for i in range(3):  # For each index from 0 to 2
    # Convert the number from numbersFirst and numbersSecond to integer
    numFirst = int(numbersFirst[i])
    numSecond = int(numbersSecond[i])
    
    # If the numbers are not equal, increase the difference count
    if numFirst != numSecond:
        differenceCount += 1

# Evaluate the number of differences
if differenceCount < 3:
    print("YES")  # Less than 3 differences
else:
    print("NO")  # 3 or more differences
