# Start the Program

# Receive Input
input_value = input()
targetNumber = abs(int(input_value))

# Initialize a Counter
index = 0

# Begin an Infinite Loop
while True:
    # Calculate the Sum of Natural Numbers
    sumOfNaturalNumbers = (index * (index + 1)) / 2
    
    # Determine the Difference from Target Number
    difference = sumOfNaturalNumbers - targetNumber
    
    # Check for Conditions
    if sumOfNaturalNumbers == targetNumber:
        print(index)
        break  # Exit the loop
    elif sumOfNaturalNumbers > targetNumber:
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop

    # Increment the Counter
    index += 1

# End the Program
