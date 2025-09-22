# Start Program

# Input: Read an integer value from user input
n = int(input())

# Initialize Boolean Array: Create a list b of size n initialized to True
boolean_array = [True] * n

# Initialize Counters: j is the current index in the array, i is the current iteration number
current_index = 0
iteration_number = 1

# Loop Until Limit: Runs while i is less than or equal to 500,000
while iteration_number <= 500000:
    # Check Boolean Condition: If the current index is True
    if boolean_array[current_index]:  
        # Mark index j as processed by setting it to False
        boolean_array[current_index] = False  
        
    # Increment the iteration number
    iteration_number += 1
    
    # Update the current index in a circular manner
    current_index = (current_index + iteration_number) % n  

# Filter True Values: Create a list x composed of elements from boolean_array that are still True
filtered_true_values = [val for val in boolean_array if val]

# Output Result: Check the length of the filtered list
if len(filtered_true_values) == 0:  
    print("YES")
else:  
    print("NO")

# End Program
