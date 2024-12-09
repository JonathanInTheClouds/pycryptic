import pytest
import os
from pycryptic.file_utils import read_file, write_file, traverse_directory

def test_read_write_file(tmp_path):
    file_path = tmp_path / "test.txt"
    data = b"This is a test file."
    
    # Write data to the file
    write_file(file_path, data)
    
    # Read data back from the file
    read_data = read_file(file_path)
    
    # Verify the data matches
    assert read_data == data

def test_traverse_directory(tmp_path):
    # Create a nested directory structure
    (tmp_path / "subdir").mkdir()
    file_1 = tmp_path / "file1.txt"
    file_2 = tmp_path / "subdir" / "file2.txt"
    file_1.write_text("File 1")
    file_2.write_text("File 2")
    
    # Traverse the directory and collect file paths
    files = list(traverse_directory(tmp_path))
    
    # Verify the correct files are found
    assert str(file_1) in files
    assert str(file_2) in files
    assert len(files) == 2

def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_file("nonexistent.txt")

def test_write_to_readonly_file(tmp_path):
    file_path = tmp_path / "readonly.txt"
    file_path.touch()  # Create the file
    file_path.chmod(0o444)  # Make it read-only
    with pytest.raises(PermissionError):
        write_file(file_path, b"Data")
