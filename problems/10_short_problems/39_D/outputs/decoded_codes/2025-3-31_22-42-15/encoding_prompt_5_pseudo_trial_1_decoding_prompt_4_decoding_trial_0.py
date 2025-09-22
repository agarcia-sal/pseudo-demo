def main():
    # Read two lines of input, each containing three integers
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count the differences
    difference_count = 0 
    
    # Loop through each element in the lists
    for index in range(3):
        # Convert each string element to an integer
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1 
    
    # Check if the count of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by executing the main function
main()
