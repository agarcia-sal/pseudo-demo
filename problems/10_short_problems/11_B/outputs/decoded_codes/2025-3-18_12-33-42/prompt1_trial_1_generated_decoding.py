# Function to calculate absolute value
def ABSOLUTE_VALUE(x):
    return abs(x)

# Read a value from user input, convert it to an integer, and take its absolute value
userInput = ABSOLUTE_VALUE(int(input()))
index = 0

# Infinite loop that continues until a break condition is met
while True:

    # Calculate the sum of the first 'index' natural numbers
    sumOfNaturalNumbers = (index * (index + 1)) / 2
    
    # Determine how much greater the sum is than the user input
    difference = sumOfNaturalNumbers - userInput
    
    # Check if the sum equals the user input
    if sumOfNaturalNumbers == userInput:
        print(index)  # Output the current index
        break  # Exit the loop
        
    # Check if the sum is greater than the user input
    elif sumOfNaturalNumbers > userInput:
        
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop
    
    # Increment the index for the next iteration
    index += 1
