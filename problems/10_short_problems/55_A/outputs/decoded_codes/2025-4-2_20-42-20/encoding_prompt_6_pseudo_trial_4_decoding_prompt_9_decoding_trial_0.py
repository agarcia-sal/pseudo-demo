# Accept an integer input representing the size of the array
size_of_array = input()  # User will input the size
array_size = int(size_of_array)  # Convert the input to an integer

# Initialize a boolean array of size 'array_size' with all values set to True
array_of_booleans = [True] * array_size  

# Initialize the index variable for the boolean array
index = 0

# Initialize a counter variable starting from 1
counter = 1

# Loop for a maximum of 500000 iterations
while counter <= 500000:
    # If the current position in the boolean array is still True
    if array_of_booleans[index]:
        # Set the current position in the boolean array to False
        array_of_booleans[index] = False
    
    # Move to the next number by incrementing the counter
    counter += 1
    
    # Calculate the new index in a circular manner
    index = (index + counter) % array_size

# Create a new list of elements from the boolean array that are still True
true_values = [value for value in array_of_booleans if value]

# Check if there are any True values left in the list
if len(true_values) == 0:
    # If there are no True values, print "YES"
    print("YES")
else:
    # If there are any True values, print "NO"
    print("NO")
