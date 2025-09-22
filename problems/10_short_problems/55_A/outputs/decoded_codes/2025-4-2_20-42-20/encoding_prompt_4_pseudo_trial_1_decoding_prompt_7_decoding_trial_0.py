# Take the number of elements in the list from the user
n = int(input())
# Create a list b of size n initialized with True values
b = [True] * n
j = 0  # Initialize j to 0
i = 1  # Initialize i to 1

# Continue the loop while i is less than or equal to 500000
while i <= 500000:
    # Check if the current index j has a True value
    if b[j]: 
        b[j] = False  # Mark current index as False
    
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update j using modulo to ensure it stays within bounds of the list

# Create a list x containing all True values from b
x = [value for value in b if value]  # Comprehension to filter for True values

# Check the length of x to determine if there are any True values remaining
if len(x) == 0:
    print('YES')  # Output 'YES' if all elements were marked False
else:
    print('NO')   # Output 'NO' if there are still True elements
