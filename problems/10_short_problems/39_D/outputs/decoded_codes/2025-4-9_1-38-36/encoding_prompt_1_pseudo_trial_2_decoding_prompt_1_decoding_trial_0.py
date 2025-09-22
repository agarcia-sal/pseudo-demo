def main_program():
    # Get the first set of numbers from user input
    first_set = read_input()
    
    # Get the second set of numbers from user input
    second_set = read_input()
    
    # Split the input strings into individual number components
    first_numbers = split_string(first_set)
    second_numbers = split_string(second_set)
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Iterate through each pair of corresponding numbers in the two sets
    for index in range(3):
        # Convert the string representation of numbers to integers
        number_from_first = convert_to_integer(first_numbers[index])
        number_from_second = convert_to_integer(second_numbers[index])
        
        # Check if the numbers are different
        if number_from_first != number_from_second:
            # Increase the count of differences
            difference_count += 1 
    
    # Check if the number of differences is less than 3
    if difference_count < 3:
        # Print "YES" if they are similar
        print("YES")
    else:
        # Print "NO" if they are not similar
        print("NO")

def read_input():
    return input()

def split_string(input_string):
    return input_string.split(" ")

def convert_to_integer(string_number):
    return int(string_number)

# Program entry point
main_program()
