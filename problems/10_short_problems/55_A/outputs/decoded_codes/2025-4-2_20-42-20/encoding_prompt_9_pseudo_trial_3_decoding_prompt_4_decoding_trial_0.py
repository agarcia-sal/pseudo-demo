def main():
    # Step 2: Accept Input
    size = int(input())
    
    # Step 3: Initialize Array
    status = [True] * size
    
    # Step 4: Set Initial Variables
    index = 0
    increment = 1
    
    # Step 5: Loop until a condition is met
    while increment <= 500000:
        # Step 5.1: Check Current Status
        if status[index]:
            status[index] = False
        
        # Step 5.2: Update Values
        increment += 1
        index = (index + increment) % size
    
    # Step 6: Filter Active Status
    active_status = [s for s in status if s]
    
    # Step 7: Determine If Any True Elements Exist
    if len(active_status) == 0:
        print("YES")
    else:
        print("NO")

# Step 8: Start the program execution
if __name__ == "__main__":
    main()
