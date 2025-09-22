# Step 1: Input the integer value representing the number of elements (n)
num_elements = int(input())

# Step 2: Initialize a list (is_prime) of size n with all values set to True
is_prime = [True] * num_elements

# Step 3: Set index variable j to 0
index = 0

# Step 4: Set counter variable i to 1
counter = 1

# Step 5: While counter is less than or equal to 500000
while counter <= 500000:
    # Step 5.1: If the value at index in list is_prime is True
    if is_prime[index]:
        # Step 5.1.1: Set the value at index in list is_prime to False
        is_prime[index] = False
    
    # Step 5.2: Increment the counter variable i by 1
    counter += 1
    
    # Step 5.3: Update the index to be the remainder of (index + counter) divided by n
    index = (index + counter) % num_elements

# Step 6: Create a new list (remaining_true) that contains all values from list is_prime that are still True
remaining_true = [value for value in is_prime if value]

# Step 7: If the length of list remaining_true is equal to 0
if len(remaining_true) == 0:
    # Output "YES"
    print("YES")
else:
    # Otherwise output "NO"
    print("NO")
