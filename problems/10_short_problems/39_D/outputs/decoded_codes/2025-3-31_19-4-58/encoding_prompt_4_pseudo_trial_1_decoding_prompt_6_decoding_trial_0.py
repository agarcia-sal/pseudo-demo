def do_main():
    # Read two lines of input for the two sets of numbers
    first_line = input()
    second_line = input()
    
    # Split the input strings into lists of integers
    first_list = list(map(int, first_line.split()))
    second_list = list(map(int, second_line.split()))
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding elements in the two lists
    for index in range(3):  # Loop for 0 to 2 inclusive
        first_number = first_list[index]  # Get the first number
        second_number = second_list[index]  # Get the second number
        
        # If the numbers are not equal, increment the difference counter
        if first_number != second_number:
            difference_count += 1
    
    # If differences are less than 3, print "YES", otherwise print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    do_main()
