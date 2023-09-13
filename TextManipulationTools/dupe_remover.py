def remove_duplicate_lines(input_file, output_file):
    seen = set()
    unique_lines = []

    with open(input_file, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line and stripped_line not in seen:
                seen.add(stripped_line)
                unique_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(unique_lines)

if __name__ == '__main__':
    source_file = input('Enter the path of the source file (press Enter for default "text.txt"): ') or 'text.txt'
    destination_file = input('Enter the path of the destination file (press Enter for default "no_duplicates.txt"): ') or 'no_duplicates.txt'
    
    remove_duplicate_lines(source_file, destination_file)
    print(f"Duplicate lines from {source_file} have been removed and saved to {destination_file}.")
