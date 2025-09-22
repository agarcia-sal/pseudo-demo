# Initialize Variables
n = int(input())
b = [True] * n
j = 0
i = 1

# Iterate to Mark Values
while i <= 500000:
    if b[j]:  # Check if the current index j in list b is 'True'
        b[j] = False  # Mark the value at index j as 'False'
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update index j

# Check Remaining True Values
x = [value for value in b if value]  # Get the True values from list b
if len(x) == 0:  # If there are no True values left
    print("YES")
else:
    print("NO")
