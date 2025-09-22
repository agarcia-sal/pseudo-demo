def main():
    # Prompting for user input
    first_input = input()
    second_input = input()
    
    # Processing the inputs
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Comparing the elements of both lists
    for index in range(3):  # Looping through the first 3 elements
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Count differences
        if first_value != second_value:
            difference_count += 1
    
    # Decide the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# If this file is executed as the main program, call the main function
if __name__ == "__main__":
    main()
