# Begin the main logic
n = int(input())  # Step 1: Read an integer from user input

# Step 2: Initialize a list 'b' with 'n' elements, all set to True
b = [True] * n  # Creating a list of True values

# Step 3: Initialize variables
j = 0  # j is the current index in the list
i = 1  # i is the step counter

# Step 4: Loop until i exceeds 500000
while i <= 500000:  # Step 4
    # Step 5: Check if the current index in list 'b' is True
    if b[j]:  # Step 5
        # Step 6: Set the current index to False
        b[j] = False  # Step 6
    
    # Step 7: Increment i by 1
    i += 1  # Step 7

    # Step 8: Update j to wrap around within bounds of 'n'
    j = (j + i) % n  # Step 8

# Step 9: Create a list 'x' of elements in 'b' that are still True
x = [value for value in b if value]  # Step 9

# Step 10: Check the length of list 'x'
if len(x) == 0:  # Step 10
    print('YES')  # If no elements are True
else:
    print('NO')  # If there are elements that are True
