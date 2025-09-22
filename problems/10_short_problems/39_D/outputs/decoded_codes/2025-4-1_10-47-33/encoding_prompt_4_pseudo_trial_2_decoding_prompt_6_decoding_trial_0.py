# Define the main function to execute the logic
def do_main():
    # Read input values for two lists of numbers
    first_list = input()
    second_list = input()
    
    # Split input strings into lists of elements
    first_list_elements = first_list.split()
    second_list_elements = second_list.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the first three elements of both lists
    for i in range(3):
        # Convert string elements to integers
        first_number = int(first_list_elements[i])
        second_number = int(second_list_elements[i])

        # If the elements are different, increment the difference counter
        if first_number != second_number:
            difference_count += 1

    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
