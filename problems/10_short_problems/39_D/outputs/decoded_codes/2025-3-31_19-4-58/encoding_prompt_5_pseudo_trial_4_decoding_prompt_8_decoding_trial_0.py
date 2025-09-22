def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()

    # Split the input lines into lists of strings
    list_first = first_line.split()
    list_second = second_line.split()
    
    # Initialize a counter to keep track of differences
    difference_count = 0 

    # Loop through each of the three numbers
    for index in range(3):
        # Convert the string numbers into integers
        number_from_first_list = int(list_first[index])
        number_from_second_list = int(list_second[index])
        
        # Check if the numbers are different
        if number_from_first_list != number_from_second_list:
            # Increment the difference counter
            difference_count += 1 
    
    # Determine the result based on the number of differences
    if difference_count < 3:
        # If there are less than 3 differences, print "YES"
        print("YES")
    else:
        # If there are 3 or more differences, print "NO"
        print("NO")

# Call the main function to execute the program
main()
