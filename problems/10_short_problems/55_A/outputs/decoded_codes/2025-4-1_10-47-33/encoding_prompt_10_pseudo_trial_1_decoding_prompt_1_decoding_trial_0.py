# Start Program

# Input:
n = int(input())  # Set `n` to the integer value read from user input.

# Initialize Boolean Array:
b = [True] * n  # Create a list `b` of size `n`, where each element is initialized to `True`.

# Initialize Counters:
j = 0  # Current index in the array.
i = 1  # Current iteration number.

# Loop Until Limit:
while i <= 500000:
    # Check Boolean Condition:
    if b[j]:  # If `b[j]` is `True`:
        b[j] = False  # Mark index `j` as processed.
    
    i += 1  # Increment `i` by 1.
    j = (j + i) % n  # Calculate the next index in a circular manner.

# Filter True Values:
x = [value for value in b if value]  # Create a list `x` composed of elements from `b` that are still `True`.

# Output Result:
if len(x) == 0:  # If the length of `x` is equal to 0:
    print("YES")  # Print "YES"
else:
    print("NO")  # Else, print "NO"

# End Program
