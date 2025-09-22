def main():
    # Read two input strings
    first_input_string = input()
    second_input_string = input()
    
    # Split the input strings into lists of substrings
    list1 = first_input_string.split()
    list2 = second_input_string.split()
    
    # Initialize a counter for differences
    difference_counter = 0 
    
    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert the current elements to integers
        value_from_list1 = int(list1[index])
        value_from_list2 = int(list2[index])
        
        # Check if the values are different
        if value_from_list1 != value_from_list2:
            difference_counter += 1  # Increment the difference counter
    
    # Check the number of differences and print the result
    if difference_counter < 3:
        print("YES")  # If differences are less than 3, print YES
    else:
        print("NO")   # Otherwise, print NO

# Start the program execution
if __name__ == "__main__":
    main()
