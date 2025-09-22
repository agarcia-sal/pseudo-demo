def main():
    # Read input from the user
    first_input = input()  # user input for the first list of numbers
    second_input = input()  # user input for the second list of numbers
    
    # Split input strings into lists
    first_list = first_input.split()  # split the first input into a list of strings
    second_list = second_input.split()  # split the second input into a list of strings
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Check the first three elements of both lists
    for index in range(3):  # loop through the first three elements
        # Convert the current elements to integers
        first_value = int(first_list[index])  # convert to integer
        second_value = int(second_list[index])  # convert to integer
        
        # Compare elements and count differences
        if first_value != second_value:  # check if the values are not equal
            difference_count += 1  # increment the counter

    # Determine result based on the number of differences
    if difference_count < 3:  # if differences are less than 3
        print("YES")  # output YES
    else:
        print("NO")  # output NO

# Entry point of the program
if __name__ == "__main__":  # check if this file is the main module
    main()  # call the main function
