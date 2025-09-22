# Start Program

# Input: Read the integer value from user input
n = int(input())

# Initialize Boolean Array: Create a list 'b' of size 'n', each element initialized to True
b = [True] * n

# Initialize Counters: Set 'j' to 0 and 'i' to 1
j = 0  # Represents the current index in the array
i = 1  # Represents the current iteration number

# Loop Until Limit: While 'i' is less than or equal to 500,000
while i <= 500000:
    # Check Boolean Condition: If 'b[j]' is True
    if b[j]:
        # Mark index 'j' as processed
        b[j] = False
    
    # Increment 'i' by 1 for the next iteration
    i += 1

    # Update 'j' to the next index in a circular manner
    j = (j + i) % n

# Filter True Values: Create a list 'x' composed of elements from 'b' that are still True
x = [value for value in b if value]

# Output Result: Check the length of 'x'
if len(x) == 0:
    print("YES")  # If no True values remain in 'x', print "YES"
else:
    print("NO")   # Otherwise, print "NO"

# End Program
