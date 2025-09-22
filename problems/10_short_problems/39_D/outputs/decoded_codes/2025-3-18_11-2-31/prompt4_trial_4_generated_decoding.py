def do_main():
    # Read two lines of input, each containing three numbers
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_numbers = first_line.split()
    second_numbers = second_line.split()
    
    # Initialize a count for differences
    difference_count = 0 
    
    # Compare corresponding numbers from both lists
    for index in range(3):
        # Convert to integer
        a = int(first_numbers[index])
        b = int(second_numbers[index])
        
        # If the numbers are different, increment the difference count
        if a != b:
            difference_count += 1
    
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()
