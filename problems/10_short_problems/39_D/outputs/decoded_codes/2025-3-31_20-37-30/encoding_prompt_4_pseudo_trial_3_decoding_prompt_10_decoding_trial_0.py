def do_main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of words
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert elements to integers for comparison
        value_a = int(first_list[index])
        value_b = int(second_list[index])
        
        # Check if the values are different
        if value_a != value_b:
            difference_count += 1
            
    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start execution of the program
do_main()
