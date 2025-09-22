def read_input():
    """Read a line of input from the user."""
    return input()

def split_string(input_string):
    """Split the input string into a list of values."""
    return input_string.split()

def convert_to_integer(value):
    """Convert a string value to an integer."""
    return int(value)

def count_discrepancies(values1, values2):
    """Count the discrepancies between the first three elements of two lists."""
    discrepancies = 0
    for index in range(3):  # Compare up to the first three elements
        value_a = convert_to_integer(values1[index])
        value_b = convert_to_integer(values2[index])
        
        if value_a != value_b:  # Increment if values are not equal
            discrepancies += 1
            
    return discrepancies

def main():
    # Read two lines of input
    input1 = read_input()
    input2 = read_input()

    # Split the input strings into lists of values
    values1 = split_string(input1)
    values2 = split_string(input2)

    # Count discrepancies
    discrepancies_count = count_discrepancies(values1, values2)

    # Print result based on the number of discrepancies
    if discrepancies_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main process
main()
