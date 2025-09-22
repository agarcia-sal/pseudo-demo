def do_main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    list1 = first_line.split()
    list2 = second_line.split()
    
    # Initialize a counter for different values
    difference_count = 0
    
    # Compare the first three elements in both lists
    for index in range(3):  # Loop through the first three elements
        # Convert the current elements to integers
        value_a = int(list1[index])
        value_b = int(list2[index])
        
        # If the values are not equal, increment the difference counter
        if value_a != value_b:
            difference_count += 1
            
    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main program execution starts here
do_main()
