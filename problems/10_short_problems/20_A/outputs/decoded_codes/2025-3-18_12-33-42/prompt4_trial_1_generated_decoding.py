def main():
    # Read input from standard input
    raw_path = input()

    # Normalize the path to ensure consistent formatting
    normalized_path = normalize_path(raw_path)

    # Output the modified path
    print(normalized_path)


def normalize_path(raw_path):
    # Trim whitespace from the beginning and end
    trimmed_path = raw_path.strip()

    # Normalize path separators and remove duplicate leading slashes
    normalized_path = normalize_separators(trimmed_path)
    
    return normalized_path


def normalize_separators(path):
    # Replace multiple leading slashes with a single leading slash
    while path.startswith('//'):
        path = '/' + path.lstrip('/')
    
    return path


if __name__ == "__main__":
    main()
