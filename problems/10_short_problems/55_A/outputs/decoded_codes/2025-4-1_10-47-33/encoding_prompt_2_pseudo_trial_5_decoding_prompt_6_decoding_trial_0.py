# Step 1: Begin the program.
# Step 2: Get an integer input from the user
total_elements = int(input())

# Step 3: Create a list called booleanList with all elements initialized to true
boolean_list = [True] * total_elements

# Step 4: Initialize variables current_index and increment
current_index = 0
increment = 1

# Step 5: Start a loop that continues while increment is less than or equal to 500,000
while increment <= 500000:
    # Step 5a: Check if the current position in boolean_list is true
    if boolean_list[current_index]:
        # Step 5a.i: Set that position in boolean_list to false
        boolean_list[current_index] = False
        
    # Step 5b: Increase the value of increment by 1
    increment += 1
    
    # Step 5c: Update current_index, ensuring it wraps around using modulo
    current_index = (current_index + increment) % total_elements

# Step 6: Create a new list containing all elements from booleanList that are still true
remaining_true_values = [value for value in boolean_list if value]

# Step 7: Check the length of remainingTrueValues
if len(remaining_true_values) == 0:
    # Step 7a: If length is 0, output "YES"
    print("YES")
else:
    # Step 7b: Otherwise, output "NO"
    print("NO")

# Step 8: End the program.
