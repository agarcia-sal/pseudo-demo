def main():
    # Read two lines of input from the user
    input_line_1 = input()
    input_line_2 = input()
    
    # Split input lines into lists
    list1 = input_line_1.split()
    list2 = input_line_2.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        value_a = int(list1[index])
        value_b = int(list2[index])
        
        # Check if the two values are different
        if value_a != value_b:
            # Increment the difference counter
            difference_count += 1
    
    # Determine the final output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()


     1 2 3
     1 2 4
     

     YES
     

     1 2 3
     1 2 3
     

     YES
     

     1 2 3
     4 5 6
     

     NO
     