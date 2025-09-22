# Get User Input
userInput = int(input())
absoluteValue = abs(userInput)

# Initialize Counter
counter = 0

# Loop to Find Solution
while True:
    # Calculate the triangular number
    triangularNumber = (counter * (counter + 1)) // 2
    # Calculate the difference
    difference = triangularNumber - absoluteValue
    
    # Check Conditions
    if triangularNumber == absoluteValue:
        print(counter)  # Print solution
        break
    elif triangularNumber > absoluteValue:
        if difference % 2 == 0:
            print(counter)  # Print solution
            break
            
    # Increment Counter
    counter += 1
