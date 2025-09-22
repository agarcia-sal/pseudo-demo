def do_main():
    # Read two lines of input
    input_line_1 = input()
    input_line_2 = input()
    
    # Split the input strings into lists of strings
    list_1 = input_line_1.split()
    list_2 = input_line_2.split()
    
    # Initialize the result counter
    difference_count = 0
    
    # Compare elements from both lists
    for index in range(3):
        a = int(list_1[index])  # Convert to integer
        b = int(list_2[index])  # Convert to integer
        
        # Increment the difference counter if values are not equal
        if a != b:
            difference_count += 1
    
    # Determine the result based on the comparison count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()
