# Step 1: Start

# Step 2: Receive Input
n = int(input())

# Step 3: Initialize List
statusList = [True] * n

# Step 4: Initialize Variables
currentIndex = 0
increment = 1

# Step 5: Process List
while increment <= 500000:
    if statusList[currentIndex] == True:
        statusList[currentIndex] = False
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Wrap around using modulo

# Step 6: Check Remaining Values
remainingTrue = [value for value in statusList if value == True]

# Step 7: Generate Output
if not remainingTrue:  # If remainingTrue is empty
    print("YES")
else:
    print("NO")

# Step 8: End
