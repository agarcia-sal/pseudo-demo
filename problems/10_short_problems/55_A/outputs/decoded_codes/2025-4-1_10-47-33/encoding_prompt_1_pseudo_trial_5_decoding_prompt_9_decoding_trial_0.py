# Input: number of elements
n = int(input())

# Initialize a list (b) with True values of size n
b = [True] * n

# Initialize variables
j = 0  # index variable
i = 1  # counter variable

# While loop to iterate until i exceeds 500000
while i <= 500000:
    # If the value at index j in list b is True
    if b[j]:
        # Set the value at index j to False
        b[j] = False
        
    # Increment the counter variable i
    i += 1
    
    # Update index j to be the remainder of (j + i) divided by n
    j = (j + i) % n

# Create a new list (x) that contains all values from b that are still True
x = [value for value in b if value]

# Check the length of list x
if len(x) == 0:
    # If list x is empty, output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")
