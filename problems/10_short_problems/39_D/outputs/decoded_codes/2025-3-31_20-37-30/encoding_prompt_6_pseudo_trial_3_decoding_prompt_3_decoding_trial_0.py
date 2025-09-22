def read_input():
    # Read a line of input from the user
    return input()

def split_string(input_line):
    # Split the input line into a list of strings based on spaces
    return input_line.split()

def convert_to_integer(string):
    # Convert a string representation of a number into an integer
    return int(string)

def main():
    # Read two lines of input containing space-separated numbers
    input_line1 = read_input()
    input_line2 = read_input()

    # Split the input lines into lists of strings
    list1 = split_string(input_line1)
    list2 = split_string(input_line2)

    # Initialize a counter for differing elements
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        number1 = convert_to_integer(list1[index])
        number2 = convert_to_integer(list2[index])
        
        # Compare the corresponding elements from both lists
        if number1 != number2:
            # Increment the counter if they differ
            difference_count += 1

    # Check if the count of differing elements is less than 3
    if difference_count < 3:
        print("YES")  # There are less than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Main execution starts here
if __name__ == "__main__":
    main()
