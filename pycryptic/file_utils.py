import os

def read_file(file_path: str) -> bytes:
    """Reads a file and returns its contents as bytes."""
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path: str, data: bytes):
    """Writes bytes to a file."""
    with open(file_path, 'wb') as file:
        file.write(data)

def traverse_directory(directory_path: str):
    """Generates file paths within a directory recursively."""
    for root, _, files in os.walk(directory_path):
        for file in files:
            yield os.path.join(root, file)
