# Start Program

# Get Input:
inp = int(input())  # Read an integer value from the user
inp = abs(inp)      # Convert the input to its absolute value

# Initialize Variables:
index = 0           # Set a variable index to 0

# Repeat Until Condition Met:
while True:         
    sum_ = index * (index + 1) // 2  # Calculate the sum of integers from 0 to index using the formula
    dif = sum_ - inp                  # Calculate the difference

    # Check Conditions:
    if sum_ == inp:                  
        print(index)                  # Print index (this is the solution) and stop the program
        break                          # Stop the program

    if sum_ > inp:                   
        if dif % 2 == 0:              # Check if dif is an even number
            print(index)              # Print index (this is the solution) and stop the program
            break                      # Stop the program
    
    index += 1                        # Increment index by 1

# End Program
