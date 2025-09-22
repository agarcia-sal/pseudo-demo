def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input strings into lists of items
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        value_from_first_line = int(first_list[index])
        value_from_second_line = int(second_list[index])
        
        # Check if the elements are different
        if value_from_first_line != value_from_second_line:
            difference_count += 1 

    # Check the number of differences and provide output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main()
