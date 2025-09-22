# Begin the program
n = int(input())  # Read an integer value from user input and store it as `n`
b = [True] * n    # Initialize a list `b` with `n` elements, all set to `True`
j = 0              # Set `j` to 0
i = 1              # Set `i` to 1

# While `i` is less than or equal to 500,000
while i <= 500000:
    if b[j]:      # Check if the element at index `j` in the list `b` is `True`
        b[j] = False  # Set it to `False`
    i += 1        # Increment `i` by 1
    j = (j + i) % n  # Update `j` to the new value

# Create a new list `x` containing all elements from `b` that are still `True`
x = [element for element in b if element]

# If the length of list `x` is 0
if len(x) == 0:
    print("YES")  # Output "YES"
else:
    print("NO")   # Output "NO"

# End the program
