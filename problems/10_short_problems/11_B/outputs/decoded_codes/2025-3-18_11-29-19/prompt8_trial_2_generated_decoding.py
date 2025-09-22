# Begin the implementation

# Read the absolute value of an integer input from the user
inputNumber = abs(int(input()))
index = 0  # This will be used to find the triangular number

# Start an infinite loop to calculate triangular numbers
while True:
    
    # Calculate the triangular number for the current index
    triangularNumber = (index * (index + 1)) // 2
    
    # Calculate the difference between triangular number and input number
    difference = triangularNumber - inputNumber
    
    # Check if the triangular number equals the input number
    if triangularNumber == inputNumber:
        print(index)  # Print the current index
        break  # Exit the loop
    
    # If the triangular number exceeds the input number
    elif triangularNumber > inputNumber:
        
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the current index
            break  # Exit the loop
    
    # Move to the next index
    index += 1

# End of implementation
