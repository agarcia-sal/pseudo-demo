# Step 1
n = int(input())  # Read an integer value n from user input

# Step 2
booleanList = [True] * n  # Create a list of size n initialized with True values
index = 0  # Set the initial index to 0
increment = 1  # Set the increment value to 1

# Step 3
while increment <= 500000:  # Explain condition to continue the loop
    if booleanList[index]:  # If the value at booleanList[index] is True
        booleanList[index] = False  # Set that index to False (indicating processed)
    
    increment += 1  # Increment the increment variable by 1
    index = (index + increment) % n  # Update index using modulo n for wrapping

# Step 4
trueValues = [value for value in booleanList if value]  # Create a list of all True values

# Step 5
if len(trueValues) == 0:  # Check if there are any True values remaining
    print("YES")  # Print "YES" if all positions were processed
else:
    print("NO")  # Print "NO" if some positions remain unprocessed
