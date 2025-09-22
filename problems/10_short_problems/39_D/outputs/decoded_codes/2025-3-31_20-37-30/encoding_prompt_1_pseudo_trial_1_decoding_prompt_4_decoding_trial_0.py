def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input strings into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values from both lists are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 

    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function
main()


1 2 3
1 2 4


5 4 3
5 4 3


10 20 30
10 21 30


7 8 9
7 8 10
