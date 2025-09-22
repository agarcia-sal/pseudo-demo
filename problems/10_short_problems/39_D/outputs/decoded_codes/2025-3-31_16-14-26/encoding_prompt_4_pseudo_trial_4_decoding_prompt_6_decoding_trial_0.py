def do_main():
    # Read two lines of input
    input_1 = input()
    input_2 = input()

    # Split the input strings into lists of strings
    list_1 = input_1.split()
    list_2 = input_2.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare corresponding elements of the two lists
    for index in range(3):
        # Convert the string values to integers
        num1 = int(list_1[index])
        num2 = int(list_2[index])
        
        # Count how many elements are different
        if num1 != num2:
            difference_count += 1 

    # Determine if differences are less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
