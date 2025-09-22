def do_main():
    # Declare variables for input
    input1 = input()
    input2 = input()
    
    # Split the inputs into lists of strings
    split_input1 = input1.split()
    split_input2 = input2.split()
    
    # Initialize difference count
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        a = int(split_input1[index])
        b = int(split_input2[index])
        
        # Check if the elements are different
        if a != b:
            difference_count += 1
            
    # Output result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
do_main()
