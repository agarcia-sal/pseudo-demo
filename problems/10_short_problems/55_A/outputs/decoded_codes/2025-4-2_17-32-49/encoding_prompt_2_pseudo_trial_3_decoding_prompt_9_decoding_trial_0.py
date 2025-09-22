# Start of the program

# Input: Read an integer value called totalNumbers
totalNumbers = int(input())

# Initialize: Create a list called isNumberAvailable with size equal to totalNumbers, all values set to True
isNumberAvailable = [True] * totalNumbers

# Initialize stepCount and currentIndex
stepCount = 1
currentIndex = 0

# Loop: Repeat while stepCount is less than or equal to 500,000
while stepCount <= 500000:
    # Check if the value at currentIndex in isNumberAvailable is True
    if isNumberAvailable[currentIndex]:
        # If it is, set that position in the list to False
        isNumberAvailable[currentIndex] = False

    # Increment stepCount by 1
    stepCount += 1
    
    # Update currentIndex using the formula `(currentIndex + stepCount) modulo totalNumbers`
    currentIndex = (currentIndex + stepCount) % totalNumbers

# Create a new list availableNumbers containing all elements from isNumberAvailable that are still True
availableNumbers = [num for num in isNumberAvailable if num]

# Check availability
if len(availableNumbers) == 0:
    print("YES")  # All numbers have been eliminated
else:
    print("NO")   # There are still available numbers

# End of the program
