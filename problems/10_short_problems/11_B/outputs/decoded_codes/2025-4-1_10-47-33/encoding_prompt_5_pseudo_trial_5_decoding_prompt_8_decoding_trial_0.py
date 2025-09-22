def find_triangular_number_index():
    target_number = abs(int(input()))
    index = 0
    
    while True:
        triangular_number = (index * (index + 1)) // 2
        difference = triangular_number - target_number
        
        if triangular_number == target_number:
            print(index)
            break
        elif triangular_number > target_number:
            if difference % 2 == 0:
                print(index)
                break
        
        index += 1

find_triangular_number_index()
