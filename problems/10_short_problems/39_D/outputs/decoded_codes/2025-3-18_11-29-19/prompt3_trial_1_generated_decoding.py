def main():
    # Get input from the user for two sets of values
    first_set = input()
    second_set = input()
    
    # Split the input strings into lists of strings
    first_list = first_set.split()
    second_list = second_set.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare the corresponding elements from both lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        # Convert the elements to integers for comparison
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # If the values are different, increment the difference counter
        if value_from_first_list != value_from_second_list:
            difference_count += 1
    
    # Check if the count of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function only if this script is run as the main program
if __name__ == "__main__":
    main()
