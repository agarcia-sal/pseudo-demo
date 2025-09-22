# Read an integer from input
n = int(input())

# Initialize a list of size n with all elements set to True
flags = [True] * n

j = 0  # Current index in the list
i = 1  # Counter used in the loop

# Loop from i=1 to i=500000 inclusive
while i <= 500000:
    if flags[j]:
        # Mark element at position j as False if it is currently True
        flags[j] = False
    
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update j to (j + i) mod n

# Collect all elements from flags that are True
true_elements = [elem for elem in flags if elem]

# Print "YES" if no True elements remain, otherwise print "NO"
if len(true_elements) == 0:
    print("YES")
else:
    print("NO")
