# Main procedure to compare two sets of numerical values

# Step 1: Input values
first_set = input()  # Read the first set of values
second_set = input()  # Read the second set of values

# Step 2: Split input strings into lists
list_first_set = first_set.split()  # Split first set into a list of strings
list_second_set = second_set.split()  # Split second set into a list of strings

# Initialize a result counter
result_count = 0  

# Step 3: Compare values
for index in range(3):  # Loop through the indices 0 to 2
    # Step 3a: Convert string values to integers
    first_value = int(list_first_set[index])  # Convert to integer
    second_value = int(list_second_set[index])  # Convert to integer
    
    # Step 3b: Check for inequality
    if first_value != second_value:  # If values are not equal
        result_count += 1  # Increment result count by 1

# Step 4: Determine result based on inequality count
if result_count < 3:  # If fewer than 3 values differed
    print("YES")  # Output affirmative result
else:
    print("NO")  # Output negative result
