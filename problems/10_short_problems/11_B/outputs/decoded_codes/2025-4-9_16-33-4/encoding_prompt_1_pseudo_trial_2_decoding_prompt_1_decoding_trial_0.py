# Start

# Get User Input
des = abs(int(input()))

# Initialize Variables
index = 0

# Begin Loop (indefinitely)
while True:
    # Calculate the sum of all integers from 1 to index
    cur = (index * (index + 1)) / 2
    
    # Calculate the difference between cur and des
    dif = cur - des
    
    # Check Conditions
    if cur == des:
        print(index)  # Found a perfect match
        break  # Exit the loop
    elif cur > des:
        if dif % 2 == 0:  # Check if dif is even
            print(index)  # Valid solution found
            break  # Exit the loop
    
    # Increment the index by 1
    index += 1

# End Program
