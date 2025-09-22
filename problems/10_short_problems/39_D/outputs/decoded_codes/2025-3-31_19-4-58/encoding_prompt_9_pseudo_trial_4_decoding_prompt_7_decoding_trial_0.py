# Start the program

# Receive input from the user for the first set of numbers
first_input = input()
# Receive input from the user for the second set of numbers
second_input = input()

# Split input into individual numbers and store them in lists
firstSet = first_input.split()
secondSet = second_input.split()

# Initialize a difference counter
differenceCount = 0

# Compare corresponding numbers in both sets
for index in range(3):  # We know there are exactly 3 elements in each set
    # Convert elements to integers from both sets
    firstNumber = int(firstSet[index])
    secondNumber = int(secondSet[index])
    
    # Check if the numbers are different
    if firstNumber != secondNumber:
        # Increment the difference count if they are different
        differenceCount += 1

# Check the number of differences and output the result
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End of program
