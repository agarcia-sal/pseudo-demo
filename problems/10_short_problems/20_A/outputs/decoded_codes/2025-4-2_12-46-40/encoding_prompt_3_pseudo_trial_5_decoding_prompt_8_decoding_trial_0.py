def readInput():
    return input().strip()

def normalizePath(inputPath):
    parts = inputPath.split('/')
    normalized = []
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if normalized:
                normalized.pop()
        else:
            normalized.append(part)
    return '/'.join(normalized)

def formatPath(normalizedPath):
    return normalizedPath.lstrip('/')

def main():
    inputPath = readInput()
    normalizedPath = normalizePath(inputPath)
    formattedPath = formatPath(normalizedPath)
    print(formattedPath)

if __name__ == "__main__":
    main()
