def main():
    # Prompt the user for two sets of numbers
    first_input = input()  # Get the first set of numbers from user input
    second_input = input()  # Get the second set of numbers from user input
    
    # Split the inputs into lists
    first_list = first_input.split()  # Split the first input into elements
    second_list = second_input.split()  # Split the second input into elements
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding elements from both lists
    for index in range(3):  # Loop over indices 0 to 2
        # Convert the current elements to integers for comparison
        number_from_first_list = int(first_list[index])  # Convert to integer from first list
        number_from_second_list = int(second_list[index])  # Convert to integer from second list
        
        # Check if the numbers are different
        if number_from_first_list != number_from_second_list:  # If they are not equal
            difference_count += 1  # Increment the difference count
    
    # Evaluate the number of differences 
    if difference_count < 3:  # If less than 3 differences were found
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# This part ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()
