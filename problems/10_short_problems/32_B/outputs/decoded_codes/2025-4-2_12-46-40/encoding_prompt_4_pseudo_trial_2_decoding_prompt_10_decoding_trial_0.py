def read_input():
    return input()

def process_input(input_string):
    index = 0
    result = ''

    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2

    return result

def main():
    input_string = read_input()
    result = process_input(input_string)
    print(result)

if __name__ == '__main__':
    main()
