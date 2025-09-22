# Read an integer n from the user, representing the size of the array.
n = int(input())

# Initialize a boolean array 'isTrue' of size n, with all elements set to True.
isTrue = [True] * n

# Set initial variables
currentIndex = 0
increment = 1

# Loop while increment is less than or equal to 500000
while increment <= 500000:
    # If isTrue[currentIndex] is True
    if isTrue[currentIndex]:
        # Mark the current index as processed
        isTrue[currentIndex] = False
    
    # Increment the increment variable by 1
    increment += 1
    
    # Update currentIndex, wrapping around the array using modulo
    currentIndex = (currentIndex + increment) % n

# Create a list 'remainingTrue' containing all elements of isTrue that are still True
remainingTrue = [value for value in isTrue if value]

# Output results
if len(remainingTrue) == 0:
    print("YES")  # Indicating all elements were processed
else:
    print("NO")   # Indicating there are elements that remain True
