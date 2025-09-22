# Start Program
number_of_elements = int(input())

# Initialize
boolean_list = [True] * number_of_elements
pointer = 0
index = 1

# Loop
while index <= 500000:
    if boolean_list[pointer]:
        boolean_list[pointer] = False
    index += 1
    pointer = (pointer + index) % number_of_elements

# Filter Active Elements
active_elements = [element for element in boolean_list if element]

# Check Result
if len(active_elements) == 0:
    print("YES")
else:
    print("NO")
