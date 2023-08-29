# File Organizer

File Organizer is a Python script that helps in tidying up your directories by automatically sorting and moving files based on their types, such as Images, Audio, Video, and Documents.

## Description

The script checks for files in the specified directory (in this case, the current directory where the script is run) and then categorizes them into folders like `Images`, `Audio`, `Video`, and `Documents` based on their file extensions. It makes the organization of files in cluttered directories more straightforward and efficient.

## Features

- Organizes files into respective folders like Images, Audio, Video, and Documents.
- Supports various common file extensions (feel free to add more):
  - Images: `.jpg`, `.jpeg`, `.png`, `.gif`
  - Audio: `.mp3`, `.wav`, `.aac`
  - Video: `.mp4`, `.mkv`, `.flv`, `.avi`
  - Documents: `.pdf`, `.docx`, `.txt`, `.xlsx`
- Provides feedback by printing the files that have been moved and their new location.

## Setup

Place the `fileorganizer.py` script in the directory you want to organize or change the `current_directory` in the script to the path of your target directory.

## Usage

After setup, simply run the script using:

```
python fileorganizer.py
```

The script will then sort the files in the directory and move them to their respective folders. You will see a series of print statements showing which files have been moved and to which folders.
