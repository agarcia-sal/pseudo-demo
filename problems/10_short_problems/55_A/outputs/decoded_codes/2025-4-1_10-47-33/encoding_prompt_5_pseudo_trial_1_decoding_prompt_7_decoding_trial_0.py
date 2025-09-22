# Start the program
n = int(input())  # Get a number 'n' from the user which indicates the size of the list

# Initialize a list 'booleanList' with 'n' elements all set to TRUE
booleanList = [True] * n

index = 0  # Set variable 'index' to 0
increment = 1  # Set variable 'increment' to 1

# WHILE increment is less than or equal to 500000 DO:
while increment <= 500000:
    # IF booleanList at position 'index' is TRUE THEN:
    if booleanList[index] is True:
        # Set booleanList at position 'index' to FALSE
        booleanList[index] = False

    increment += 1  # Increase increment by 1
    index = (index + increment) % n  # Update index to (index + increment) modulo n

# Create a new list 'remainingTrue' that contains all TRUE values from booleanList
remainingTrue = [value for value in booleanList if value is True]

# IF the length of remainingTrue is 0 THEN:
if len(remainingTrue) == 0:
    print("YES")  # PRINT "YES"
else:
    print("NO")  # PRINT "NO"

# End of the program
