# Read an integer value n which represents the number of elements.
n = int(input())

# Initialize a list isTrue of size n filled with True values.
isTrue = [True] * n
currentIndex = 0  # set an integer variable currentIndex to 0
step = 1          # set an integer variable step to 1

# Loop until step exceeds 500,000
while step <= 500000:
    # Check if the value at position currentIndex in isTrue is True
    if isTrue[currentIndex]:
        # If it is True, set that position in isTrue to False
        isTrue[currentIndex] = False
        
    # Increment step by 1
    step += 1
    
    # Update currentIndex using the formula (currentIndex + step) mod n
    currentIndex = (currentIndex + step) % n

# Filter: Create a new list remainingTrue that contains all True values from isTrue
remainingTrue = [value for value in isTrue if value]

# Check outcome
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
