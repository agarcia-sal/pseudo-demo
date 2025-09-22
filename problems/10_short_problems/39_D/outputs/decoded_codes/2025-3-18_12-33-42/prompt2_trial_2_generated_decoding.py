# Begin the program

# Declare a variable to hold the first input string
first_input = ""
# Declare a variable to hold the second input string
second_input = ""

# Read the first input from the user and store it in the first input variable
first_input = input()
# Read the second input from the user and store it in the second input variable
second_input = input()

# Split the first input string into a list of substrings
first_input_list = first_input.split()
# Split the second input string into a list of substrings
second_input_list = second_input.split()

# Initialize a variable to count differences
differences_count = 0

# For each index from 0 to 2 (inclusive), perform the following steps
for index in range(3):
    # Convert the substring from the first list at the current index into an integer
    first_number = int(first_input_list[index])
    # Convert the substring from the second list at the same index into an integer
    second_number = int(second_input_list[index])
    
    # If firstNumber is not equal to secondNumber
    if first_number != second_number:
        # Increment the differences count by one
        differences_count += 1

# If the count of differences is less than 3
if differences_count < 3:
    # Output "YES"
    print("YES")
# Otherwise
else:
    # Output "NO"
    print("NO")

# End the program
