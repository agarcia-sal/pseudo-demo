s = input().strip()

index = 0
result = ""

while index < len(s):
    if s[index] == '.':
        result += '0'
        index += 1
    else:
        if index + 1 < len(s) and s[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2

print(result)
