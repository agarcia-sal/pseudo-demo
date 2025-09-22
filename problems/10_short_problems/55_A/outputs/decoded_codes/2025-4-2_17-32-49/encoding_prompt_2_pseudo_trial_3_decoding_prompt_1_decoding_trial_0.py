# Start

# Input: Read an integer value called totalNumbers
totalNumbers = int(input())

# Initialize: Create a list called isNumberAvailable with size equal to totalNumbers, all values set to True
isNumberAvailable = [True] * totalNumbers  # List of booleans initialized to True

# Initialize: Set a variable stepCount to 1
stepCount = 1  

# Initialize: Set a variable currentIndex to 0
currentIndex = 0  

# Loop: Repeat while stepCount is less than or equal to 500,000
while stepCount <= 500000:
    # Check if the value at currentIndex in isNumberAvailable list is True
    if isNumberAvailable[currentIndex]:
        isNumberAvailable[currentIndex] = False  # Set that position in the list to False

    # Increment stepCount by 1
    stepCount += 1 

    # Update currentIndex
    currentIndex = (currentIndex + stepCount) % totalNumbers  # Calculate new current position

# Create a new list: Generate a list called availableNumbers
availableNumbers = [index for index, available in enumerate(isNumberAvailable) if available]

# Check availability
if len(availableNumbers) == 0:
    # Output "YES"
    print("YES")  # All numbers have been eliminated
else:
    # Output "NO"
    print("NO")  # There are still available numbers

# End
