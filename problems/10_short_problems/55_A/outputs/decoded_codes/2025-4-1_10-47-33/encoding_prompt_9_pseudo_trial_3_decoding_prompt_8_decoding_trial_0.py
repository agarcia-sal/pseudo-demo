# Start

# Receive Input
n = int(input())

# Initialize List
statusList = [True] * n  # Create a list of size n with all values set to True

# Initialize Variables
currentIndex = 0
increment = 1

# Process List
while increment <= 500000:
    if statusList[currentIndex]:  # Check if the current index is True
        statusList[currentIndex] = False  # Change the value to False
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Update index with wrap around

# Check Remaining Values
remainingTrue = [value for value in statusList if value]  # Create a list of remaining True values

# Generate Output
if not remainingTrue:  # If there are no True values left
    print("YES")
else:
    print("NO")

# End
