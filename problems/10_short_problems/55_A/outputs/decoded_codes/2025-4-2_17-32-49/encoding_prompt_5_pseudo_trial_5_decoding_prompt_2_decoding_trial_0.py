# Start Program

# Input Section
n = int(input())  # Prompt the user to enter a number n and convert it to an integer

# Initialization
booleanList = [True] * n  # Create a list with n elements, all set to True
currentIndex = 0  # Set the current index to 0
counter = 1  # Set the counter to 1

# Loop for Operations
while counter <= 500000:
    if booleanList[currentIndex]:  # If the current element is True
        booleanList[currentIndex] = False  # Change this element to False
    
    counter += 1  # Increment counter by 1
    currentIndex = (currentIndex + counter) % n  # Update current index

# Check Remaining True Values
remainingTrue = [value for value in booleanList if value]  # List of remaining True elements

if len(remainingTrue) == 0:  # If there are no remaining True values
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# End Program
