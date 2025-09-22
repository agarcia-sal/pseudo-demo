def read_input():
    """Reads a line of input from the user."""
    return input()

def split_string(input_string):
    """Splits a string by whitespace and returns a list of values."""
    return input_string.split()

def convert_to_integer(value):
    """Converts a string value to an integer."""
    return int(value)

def start_main():
    # Read two lines of input
    input1 = read_input()
    input2 = read_input()

    # Split the input strings into lists of values
    values1 = split_string(input1)
    values2 = split_string(input2)

    # Initialize a counter for discrepancies
    count_discrepancies = 0 

    # Compare the elements of both lists up to the first three elements
    for index in range(3):
        # Convert the current elements to integers
        valueA = convert_to_integer(values1[index])
        valueB = convert_to_integer(values2[index])
        
        # If the values are not equal, increment the discrepancy counter
        if valueA != valueB:
            count_discrepancies += 1 

    # If there are fewer than three discrepancies, print "YES"; otherwise print "NO"
    if count_discrepancies < 3:
        print("YES")
    else:
        print("NO")

# Start the main process
start_main()
