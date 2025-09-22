# Start by reading an integer input which represents a number called total_count.
total_count = int(input())

# Create a list named boolean_array of size total_count, initializing all values to True.
boolean_array = [True] * total_count

# Initialize two variables: increment_value to 1 and index to 0.
increment_value = 1
index = 0

# Begin a loop that continues as long as increment_value is less than or equal to 500,000.
while increment_value <= 500000:
    # Check if the current position in boolean_array (at index) holds a value of True.
    if boolean_array[index]:
        # Change the value at that position (index) in boolean_array to False.
        boolean_array[index] = False

    # Increase increment_value by 1.
    increment_value += 1
    
    # Update index by adding increment_value to it and taking the modulus with total_count.
    index = (index + increment_value) % total_count

# Create a new list named true_values which contains all the positions in boolean_array that are still True.
true_values = [i for i, value in enumerate(boolean_array) if value]

# Check the size of true_values.
if len(true_values) == 0:
    # If true_values is empty, print "YES".
    print("YES")
else:
    # Otherwise, print "NO".
    print("NO")
