def main():
    # Read two lines of input
    inputLine1 = input()
    inputLine2 = input()
    
    # Split the input lines into lists of strings
    list1 = inputLine1.split()
    list2 = inputLine2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from both lists to integers
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the values are different
        if value1 != value2:
            # Increment the difference counter
            differenceCount += 1
            
    # If the number of differences is less than 3, print "YES", otherwise print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
