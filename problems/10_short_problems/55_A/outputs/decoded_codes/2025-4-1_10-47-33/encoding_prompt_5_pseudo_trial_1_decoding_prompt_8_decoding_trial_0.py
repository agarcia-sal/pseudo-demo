# Start the program
n = int(input())  # Get a number 'n' from the user which indicates the size of the list
booleanList = [True] * n  # Initialize a list 'booleanList' with 'n' elements all set to TRUE
index = 0  # Set variable 'index' to 0
increment = 1  # Set variable 'increment' to 1

while increment <= 500000:  # WHILE increment is less than or equal to 500000 DO:
    if booleanList[index]:  # IF booleanList at position 'index' is TRUE THEN:
        booleanList[index] = False  # Set booleanList at position 'index' to FALSE
    increment += 1  # Increase increment by 1
    index = (index + increment) % n  # Update index to (index + increment) modulo n

remainingTrue = [value for value in booleanList if value]  # Create a new list 'remainingTrue' that contains all TRUE values

if len(remainingTrue) == 0:  # IF the length of remainingTrue is 0 THEN:
    print("YES")  # PRINT "YES"
else:  # ELSE:
    print("NO")  # PRINT "NO"

# End the program
