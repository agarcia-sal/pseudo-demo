# Start the program
# Get a number 'n' from the user which indicates the size of the list
n = int(input())

# Initialize a list 'booleanList' with 'n' elements all set to TRUE
booleanList = [True] * n

# Set variable 'index' to 0
index = 0

# Set variable 'increment' to 1
increment = 1

# WHILE increment is less than or equal to 500000
while increment <= 500000:
    # IF booleanList at position 'index' is TRUE
    if booleanList[index] == True:
        # Set booleanList at position 'index' to FALSE
        booleanList[index] = False
    
    # Increase increment by 1
    increment += 1
    
    # Update index to (index + increment) modulo n to wrap around if it exceeds n
    index = (index + increment) % n

# Create a new list 'remainingTrue' that contains all TRUE values from booleanList
remainingTrue = [value for value in booleanList if value == True]

# IF the length of remainingTrue is 0
if len(remainingTrue) == 0:
    # PRINT "YES"
    print("YES")
else:
    # PRINT "NO"
    print("NO")

# End the program
