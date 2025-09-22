# Start the program

# Step 2: Receive two input strings representing two sets of three numbers
firstSet = input()
secondSet = input()

# Step 3: Split both input strings into lists
# Create a list called `numbersFirst` by dividing `firstSet`
numbersFirst = firstSet.split()
# Create a list called `numbersSecond` by dividing `secondSet`
numbersSecond = secondSet.split()

# Step 4: Initialize a counter for differences
differenceCount = 0

# Step 5: Loop through each number in both lists
for index in range(3):  # We know there are exactly three numbers, so we loop from 0 to 2
    # Convert the number from both lists to integers
    numFirst = int(numbersFirst[index])
    numSecond = int(numbersSecond[index])
    
    # Check for differences
    if numFirst != numSecond:
        differenceCount += 1  # Increment the counter if numbers differ

# Step 6: Evaluate the number of differences
if differenceCount < 3:
    print("YES")  # Less than 3 differences
else:
    print("NO")   # 3 or more differences

# End of the program
