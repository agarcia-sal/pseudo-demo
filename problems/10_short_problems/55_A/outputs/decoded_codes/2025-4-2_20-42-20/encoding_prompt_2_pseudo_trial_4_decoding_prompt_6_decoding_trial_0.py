# Step 1: Read an integer value n from the user
array_size = int(input())

# Step 2: Initialize an array isPrime of size n with all values set to True
is_prime = [True] * array_size

# Step 3: Set currentIndex to 0
current_index = 0

# Step 4: Set step to 1
step = 1

# Step 5: Begin a loop that continues as long as step is less than or equal to 500,000
while step <= 500000:
    # Step 6: Check if the value at position currentIndex in isPrime is True
    if is_prime[current_index]:
        # If it is True, change it to False (marking it as not prime)
        is_prime[current_index] = False
    
    # Increment step by 1
    step += 1
    
    # Update currentIndex
    current_index = (current_index + step) % array_size

# Step 7: Create a new list untouchedIndices with all values from isPrime that remain True
untouched_indices = [index for index, value in enumerate(is_prime) if value]

# Step 8: Check the length of untouchedIndices
if len(untouched_indices) == 0:
    print("YES")
else:
    print("NO")
