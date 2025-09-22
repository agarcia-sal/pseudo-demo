# Start

# Input: Read an integer value called totalNumbers
totalNumbers = int(input())

# Initialize: Create a list called isNumberAvailable with size equal to totalNumbers, and set all values to True
isNumberAvailable = [True] * totalNumbers

# Initialize: Set a variable stepCount to 1 to track the current step in the elimination process
stepCount = 1

# Initialize: Set a variable currentIndex to 0 to indicate the current position in the isNumberAvailable list
currentIndex = 0

# Loop: Repeat while stepCount is less than or equal to 500,000
while stepCount <= 500000:
    # Check if the value at currentIndex in the isNumberAvailable list is True
    if isNumberAvailable[currentIndex]:
        # If it is, set that position in the list to False
        isNumberAvailable[currentIndex] = False
        
    # Increment stepCount by 1
    stepCount += 1
    
    # Update currentIndex to be the new current position using the formula (currentIndex + stepCount) modulo totalNumbers
    currentIndex = (currentIndex + stepCount) % totalNumbers

# Create a new list: Generate a list called availableNumbers containing all elements from isNumberAvailable that remain True
availableNumbers = [num for num in isNumberAvailable if num]

# Check availability
if len(availableNumbers) == 0:
    # Output “YES” (indicating all numbers have been eliminated)
    print("YES")
else:
    # Output “NO” (indicating there are still available numbers)
    print("NO")

# End
