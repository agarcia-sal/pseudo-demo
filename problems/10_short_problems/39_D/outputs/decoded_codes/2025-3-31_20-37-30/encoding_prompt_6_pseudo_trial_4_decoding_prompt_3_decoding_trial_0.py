def split_string(input_string):
    # Split the string on spaces and return the list of numbers as strings
    return input_string.split()

def convert_to_integer(number_string):
    # Convert string to integer
    return int(number_string)

def main():
    # Step 1: Get two lines of input from the user
    first_string = input()
    second_string = input()

    # Step 2: Split the input strings into lists of numbers
    first_list = split_string(first_string)
    second_list = split_string(second_string)

    # Step 3: Initialize a counter to track differences
    difference_count = 0 

    # Step 4: Compare the numbers in each list
    for index in range(3):
        first_number = convert_to_integer(first_list[index])
        second_number = convert_to_integer(second_list[index])
        
        # Step 5: Check if the numbers are different
        if first_number != second_number:
            difference_count += 1 

    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
