def main():
    # Read two lines of input containing space-separated numbers
    input_line_1 = input()
    input_line_2 = input()

    # Split the input lines into lists of strings
    list1 = input_line_1.split()
    list2 = input_line_2.split()

    # Initialize a counter for differing elements
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        number1 = int(list1[index])
        number2 = int(list2[index])
        
        # Compare the corresponding elements from both lists
        if number1 != number2:
            # Increment the counter if they differ
            difference_count += 1

    # Check if the count of differing elements is less than 3
    if difference_count < 3:
        print("YES")  # There are less than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Main execution starts here
main()
