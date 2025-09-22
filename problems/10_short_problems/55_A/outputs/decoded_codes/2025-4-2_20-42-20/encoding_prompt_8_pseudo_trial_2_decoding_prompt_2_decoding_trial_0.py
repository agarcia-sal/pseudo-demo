# 1. Initialize Variables
n = int(input())  # Read an integer value `n` from user input
b = [True] * n    # Create a list `b` of size `n` filled with 'True' values
j = 0              # Set `j` to 0 (index tracker)
i = 1              # Set `i` to 1 (steps tracker)

# 2. Iterate to Mark Values
while i <= 500000:
    if b[j]:      # Check if the current index `j` in list `b` is 'True'
        b[j] = False  # Mark the value at index `j` as 'False'
    
    i += 1        # Increment `i` by 1
    j = (j + i) % n  # Update index `j` based on the sum and wrap around using modulo `n`

# 3. Check Remaining True Values
x = [value for value in b if value]  # Create a list `x` containing only the 'True' values from list `b`
if len(x) == 0:  # If the length of `x` is 0
    print("YES")  # Output "YES"
else:
    print("NO")   # Output "NO"
