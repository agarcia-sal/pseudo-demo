# Start Program

# Input Section
n = int(input())  # Prompt the user to enter a number n

# Initialization
booleanList = [True] * n  # Create a list booleanList with n elements, all initially set to True
currentIndex = 0  # Set currentIndex to 0
counter = 1  # Set counter to 1

# Loop for Operations
while counter <= 500000:
    if booleanList[currentIndex]:  # If the current element is True
        booleanList[currentIndex] = False  # Change this element to False
    
    counter += 1  # Increment counter by 1
    currentIndex = (currentIndex + counter) % n  # Update currentIndex

# Check Remaining True Values
remainingTrue = [x for x in booleanList if x]  # Create remainingTrue as list of True elements in booleanList

if len(remainingTrue) == 0:  # If length of remainingTrue is 0
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# End Program
