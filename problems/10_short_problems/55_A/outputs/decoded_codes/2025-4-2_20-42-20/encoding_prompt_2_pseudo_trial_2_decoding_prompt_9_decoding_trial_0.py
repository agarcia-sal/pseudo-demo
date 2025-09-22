# Start the program by receiving an integer input for the number of elements in the list
number_of_elements = int(input())

# Create a list called "flags" initialized to True for the specified number of elements
flags = [True] * number_of_elements

# Initialize "index" to 0 and "counter" to 1
index = 0
counter = 1

# Loop while "counter" is less than or equal to 500,000
while counter <= 500000:
    # If the current entry in "flags" at position "index" is True
    if flags[index]:
        # Set that entry to False
        flags[index] = False
    # Increment "counter" to proceed to the next iteration
    counter += 1
    # Update "index" using modular arithmetic to wrap around the flags list
    index = (index + counter) % number_of_elements

# Create a new list called "active_flags" that includes only the entries from "flags" that are still True
active_flags = [flag for flag in flags if flag]

# Check the length of "active_flags"
if len(active_flags) == 0:
    print("YES")  # If empty, output "YES"
else:
    print("NO")   # If not empty, output "NO"
