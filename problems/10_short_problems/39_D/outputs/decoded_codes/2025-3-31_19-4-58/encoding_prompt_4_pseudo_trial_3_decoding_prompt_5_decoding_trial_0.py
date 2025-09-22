def do_main():
    # Initialize variables to hold user inputs and the difference count
    input1 = input()
    input2 = input()
    difference_count = 0
    
    # Split the inputs into lists
    split_input1 = input1.split()
    split_input2 = input2.split()

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
