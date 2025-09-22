# Start Program

# Get Input:
inp = int(input())
inp = abs(inp)  # Convert input to absolute value

# Initialize Variables:
index = 0  # Keep track of the current number we are evaluating

# Repeat Until Condition Met:
while True:
    # Calculate sum_ as the sum of all integers from 0 to index
    sum_ = index * (index + 1) // 2  # Using integer division to keep it an integer
    dif = sum_ - inp  # Calculate the difference

    # Check Conditions:
    if sum_ == inp:
        print(index)  # Print index (this is the solution) and stop the program
        break  # Exiting the while loop

    if sum_ > inp:
        if dif % 2 == 0:  # Check if dif is an even number
            print(index)  # Print index (this is the solution) and stop the program
            break  # Exiting the while loop

    # Increment index by 1
    index += 1

# End Program
