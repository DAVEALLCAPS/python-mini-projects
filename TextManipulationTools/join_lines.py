def join_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]
        joined_text = ' '.join(lines)

    with open(output_file, 'w') as f:
        f.write(joined_text)

if __name__ == '__main__':
    source_file = input('Enter the path of the source file (press Enter for default "text.txt"): ') or 'text.txt'
    destination_file = input('Enter the path of the destination file (press Enter for default "joined.txt"): ') or 'joined.txt'
    join_lines(source_file, destination_file)
    print(f"Lines from {source_file} have been joined and saved to {destination_file}.")
