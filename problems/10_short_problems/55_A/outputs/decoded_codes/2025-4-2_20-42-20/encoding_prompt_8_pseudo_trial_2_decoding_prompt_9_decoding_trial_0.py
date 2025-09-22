# Initialize variables
n = int(input())  # Read an integer value for the size of the list
b = [True] * n    # Create a list 'b' of size 'n' initialized to True
j = 0              # Initialize index j to 0
i = 1              # Initialize step counter i to 1

# Iterate to mark values
while i <= 500000:
    if b[j]:  # Check if the current index j in list b is True
        b[j] = False  # Mark index j as False
        
    i += 1  # Increment the step counter
    j = (j + i) % n  # Update index j, wrapping around using modulo n

# Check remaining True values
x = [value for value in b if value]  # Create a list of remaining True values

if len(x) == 0:  # If there are no True values left
    print("YES")  # Output "YES"
else:
    print("NO")   # Otherwise, output "NO"
