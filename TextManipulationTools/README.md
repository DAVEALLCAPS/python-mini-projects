# Text Manipulation Tools

`text_tools.py` is a command-line script offering two main utilities: joining lines and removing duplicate lines from a given text file.

## Features
- **Join Lines**: Combines lines from a source file into one continuous line.
- **Remove Duplicates**: Removes duplicate lines, ensuring each line in the output is unique.

## Usage
```
py text_tools.py [source_filename] <action>
```

### Actions:
- `--joiner`: Joins lines from the source file.
- `--dupes`: Removes duplicate lines from the source file.

### Options:
- `source_filename`: Specify the source file. If omitted, defaults to 'text.txt'.

### Examples:
1. To join lines using the default source file `text.txt`:
   ```
   py text_tools.py --joiner
   ```
2. To remove duplicates from a specific source file:
   ```
   py text_tools.py source_filename.txt --dupes
   ```
3. For help:
   ```
   py text_tools.py --help
   ```

### Output
The script outputs to a file named `output.txt` by default.
