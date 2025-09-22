# Step 1: Reading input
totalCount = int(input())  # Read an integer input for totalCount

# Step 2: Creating the boolean array
booleanArray = [True] * totalCount  # Create an array of size totalCount, initialized to True

# Step 3: Initializing variables
incrementValue = 1  # Initialize incrementValue to 1
index = 0  # Initialize index to 0

# Step 4: Begin the loop
while incrementValue <= 500000:  # Loop until incrementValue is less than or equal to 500,000
    if booleanArray[index]:  # Check if the value at current index is True
        booleanArray[index] = False  # Set the value at index to False

    incrementValue += 1  # Increase incrementValue by 1
    index = (index + incrementValue) % totalCount  # Update index with wrap around using modulus

# Step 5: Creating the new list of true values
trueValues = [i for i in range(totalCount) if booleanArray[i]]  # Collect indices where booleanArray is True

# Step 6: Checking the size of trueValues
if len(trueValues) == 0:  # If trueValues is empty
    print("YES")  # Print "YES"
else:
    print("NO")  # Otherwise, print "NO"
