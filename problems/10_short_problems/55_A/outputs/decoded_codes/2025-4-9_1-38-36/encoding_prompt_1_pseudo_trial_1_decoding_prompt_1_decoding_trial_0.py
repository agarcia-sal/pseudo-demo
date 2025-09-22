# Step 1: Get a number 'n' from user input
n = int(input())

# Step 2: Create a list called 'booleanList' with 'n' elements, all initialized to True
booleanList = [True] * n

# Step 3: Initialize two counters: 'j' to 0 and 'i' to 1
j = 0
i = 1

# Step 4: While 'i' is less than or equal to 500,000 do the following:
while i <= 500000:
    # Step 4a: If the element at index 'j' in 'booleanList' is True:
    if booleanList[j]:
        # Step 4ai: Set the element at index 'j' in 'booleanList' to False
        booleanList[j] = False  # Mark this index as not meeting the condition

    # Step 4b: Increment 'i' by 1
    i += 1
    
    # Step 4c: Update 'j' to the new index by adding 'i' and taking the remainder when divided by 'n'
    j = (j + i) % n  # This wraps around if 'j' exceeds 'n - 1'

# Step 5: Create a new list called 'remainingTrueValues' that contains only the elements from 'booleanList' that are still True
remainingTrueValues = [value for value in booleanList if value]

# Step 6: If 'remainingTrueValues' is empty:
if not remainingTrueValues:
    # Step 6a: Print 'YES' 
    print('YES')  # There are no True values left
# Step 7: Otherwise:
else:
    # Step 7a: Print 'NO'
    print('NO')  # There are still True values present
