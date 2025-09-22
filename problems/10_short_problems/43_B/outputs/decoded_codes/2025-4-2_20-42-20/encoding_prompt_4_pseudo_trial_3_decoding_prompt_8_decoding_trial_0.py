def remove_spaces(input_string):
    return ''.join(character for character in input_string if character != ' ')

def count_character(string, character_code):
    character = chr(character_code)
    return string.count(character)

def count_negative(lst):
    return sum(1 for x in lst if x < 0)

# Main program logic
first_string = input()
second_string = input()

s1 = remove_spaces(first_string)
s2 = remove_spaces(second_string)

frequency_differences = []

for character_code in range(ord('A'), ord('z') + 1):
    frequency_in_s1 = count_character(s1, character_code)
    frequency_in_s2 = count_character(s2, character_code)
    frequency_difference = frequency_in_s1 - frequency_in_s2
    frequency_differences.append(frequency_difference)

if count_negative(frequency_differences) == 0:
    print("YES")
else:
    print("NO")
