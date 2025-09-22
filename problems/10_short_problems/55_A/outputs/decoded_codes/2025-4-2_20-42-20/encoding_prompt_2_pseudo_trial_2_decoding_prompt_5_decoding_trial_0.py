# Start the program by receiving an integer input for the number of elements in the list
number_of_elements = int(input())

# Create a list called "flags" with "number_of_elements" entries, all initially set to True
flags = [True] * number_of_elements

# Initialize index and counter variables
index = 0
counter = 1

# Loop as long as counter is less than or equal to 500,000
while counter <= 500000:
    # If the current entry in "flags" at position "index" is True
    if flags[index]:
        # Set that entry to False
        flags[index] = False
    
    # Increment counter by 1
    counter += 1
    
    # Update index while wrapping around using remainder
    index = (index + counter) % number_of_elements

# Create a new list called "active_flags" that includes only the entries from "flags" that are still True
active_flags = [flag for flag in flags if flag]

# Check the length of the "active_flags" list
if len(active_flags) == 0:
    # If empty, output "YES"
    print("YES")
else:
    # If not empty, output "NO"
    print("NO")
