# Start
# Get User Input
des = abs(int(input()))

# Initialize Variables
index = 0

# Begin Loop (indefinitely)
while True:
    # Calculate the sum of all integers from 1 to index
    cur = (index * (index + 1)) // 2  # Using integer division to avoid float results

    # Calculate the difference between cur and des
    dif = cur - des

    # Check Conditions
    if cur == des:
        print(index)  # Found a perfect match
        break
    elif cur > des:
        if dif % 2 == 0:  # Check if dif is even
            print(index)  # Valid solution
            break

    # Increment the index by 1
    index += 1

# End Loop
# End Program
