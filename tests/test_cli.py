import subprocess

def test_cli_encrypt_decrypt(tmp_path):
    """Test encryption and decryption using the CLI."""
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.enc"
    decrypted_file = tmp_path / "decrypted.txt"
    password = "mypassword"

    # Write sample data to input file
    input_file.write_text("Hello, CLI Test!")

    # Run encryption
    result_encrypt = subprocess.run(
        ["python", "-m", "pycryptic.cli", "encrypt", str(input_file), str(output_file), "--password", password],
        capture_output=True,
        text=True,
    )
    assert result_encrypt.returncode == 0  # Ensure success
    assert output_file.exists()

    # Run decryption
    result_decrypt = subprocess.run(
        ["python", "-m", "pycryptic.cli", "decrypt", str(output_file), str(decrypted_file), "--password", password],
        capture_output=True,
        text=True,
    )
    assert result_decrypt.returncode == 0  # Ensure success
    assert decrypted_file.exists()
    assert decrypted_file.read_text() == "Hello, CLI Test!"

def test_cli_encrypt_invalid_input():
    """Test CLI behavior with invalid input file."""
    result = subprocess.run(
        ["python", "-m", "pycryptic.cli", "encrypt", "nonexistent.txt", "output.enc", "--password", "mypassword"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0  # Ensure the command fails
    assert "Error: Input path 'nonexistent.txt' does not exist." in result.stderr

def test_cli_missing_args():
    """Test CLI behavior with missing arguments."""
    result = subprocess.run(
        ["python", "-m", "pycryptic.cli"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0  # Ensure failure
    assert "usage: " in result.stderr.lower()  # Ensure help message is displayed

def test_cli_directory_encrypt_decrypt(tmp_path):
    """
    Test encrypting and decrypting all files in a directory via the CLI.
    """
    # Setup: Create a directory structure with some files
    input_dir = tmp_path / "input_dir"
    input_dir.mkdir()
    (input_dir / "file1.txt").write_text("Content of file 1")
    (input_dir / "file2.txt").write_text("Content of file 2")
    subdir = input_dir / "subdir"
    subdir.mkdir()
    (subdir / "file3.txt").write_text("Content of file 3")

    # Paths for output and decrypted directories
    encrypted_dir = tmp_path / "encrypted_dir"
    decrypted_dir = tmp_path / "decrypted_dir"

    # Encrypt the directory
    subprocess.run(
        ["python", "-m", "pycryptic.cli", "encrypt", str(input_dir), str(encrypted_dir), "--password", "mypassword"],
        check=True
    )

    # Ensure the encrypted directory exists and has the same structure
    assert (encrypted_dir / "file1.txt").exists()
    assert (encrypted_dir / "file2.txt").exists()
    assert (encrypted_dir / "subdir" / "file3.txt").exists()

    # Decrypt the directory
    subprocess.run(
        ["python", "-m", "pycryptic.cli", "decrypt", str(encrypted_dir), str(decrypted_dir), "--password", "mypassword"],
        check=True
    )

    # Ensure the decrypted files match the original contents
    assert (decrypted_dir / "file1.txt").read_text() == "Content of file 1"
    assert (decrypted_dir / "file2.txt").read_text() == "Content of file 2"
    assert (decrypted_dir / "subdir" / "file3.txt").read_text() == "Content of file 3"
