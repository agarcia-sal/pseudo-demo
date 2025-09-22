# Start

# Receive Input:
list_size = int(input())

# Initialize Boolean List:
boolean_list = [True] * list_size

# Initialize Iteration Variables:
current_index = 0
step = 1

# Loop through iterations:
while step <= 500000:
    if boolean_list[current_index]:
        boolean_list[current_index] = False
    step += 1
    current_index = (current_index + step) % list_size

# Check Remaining True Values:
remaining_true = [value for value in boolean_list if value]

# Output Result:
if len(remaining_true) == 0:
    print("YES")
else:
    print("NO")

# End
