# Step 1: Accept an integer input that specifies the size of a list
n = int(input())

# Step 2: Create a list of boolean values, initializing each value to True
boolean_list = [True] * n

# Step 3: Initialize index and current position variables
index = 1
current_position = 0

# Step 4: Enter a loop that continues as long as the index is less than or equal to 500,000
while index <= 500000:
    # Check if the current position in the boolean list has a True value
    if current_position < n and boolean_list[current_position]:
        # If it does, change that value to False
        boolean_list[current_position] = False
    
    # Increment the index by 1
    index += 1
    
    # Update the current position using the formula
    current_position = (current_position + index) % n

# Step 5: Create a new list by filtering the boolean list to include only the True values
filtered_list = [value for value in boolean_list if value]

# Step 6: Check the length of the filtered list
if len(filtered_list) == 0:
    # If the length is zero, output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")
