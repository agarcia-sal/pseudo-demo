# Start by reading an integer input which represents a number called totalCount
total_count = int(input())

# Create an array named boolean_array of size totalCount, initializing all values to True
boolean_array = [True] * total_count

# Initialize two variables
increment_value = 1  # This will control the loop iterations
index = 0  # This will track the current position in the boolean_array

# Begin a loop that continues as long as incrementValue is less than or equal to 500,000
while increment_value <= 500000:
    # Check if the current position in the boolean_array (at index) holds a value of True
    if boolean_array[index]:
        # Change the value at that position in boolean_array to False
        boolean_array[index] = False
    
    # Increase increment_value by 1
    increment_value += 1
    
    # Update index by adding increment_value to it and taking the modulus with totalCount
    index = (index + increment_value) % total_count

# Create a new list called true_values which contains all the positions in boolean_array that are still True
true_values = [i for i, value in enumerate(boolean_array) if value]

# Check the size of true_values
if len(true_values) == 0:
    print("YES")
else:
    print("NO")
