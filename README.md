# PyCryptic

**PyCryptic** is a Python-based command-line tool for encrypting and decrypting files and directories using AES encryption. It ensures data security by allowing users to provide their own passwords for encryption and decryption. Designed to be simple, robust, and efficient, PyCryptic is a great solution for securing sensitive information.

---

## Features

- **File Encryption**: Encrypt single files securely using AES.
- **Directory Encryption**: Recursively encrypt all files within a directory.
- **File Decryption**: Decrypt encrypted files with the correct password.
- **Cross-Platform**: Works seamlessly on Linux, macOS, and Windows.
- **Custom Passwords**: Users can specify their own password for encryption and decryption.

---

## Installation

### Prerequisites
- Python 3.10 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pycryptic.git
   cd pycryptic
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Install PyCryptic in editable mode:
   ```bash
   pip install -e .
   ```

---

## Usage

### Basic Syntax
```bash
python -m pycryptic.cli <action> <input_path> <output_path> --password <password>
```

### Arguments
- `<action>`: `encrypt` or `decrypt`
- `<input_path>`: Path to the file or directory to process
- `<output_path>`: Path to the output file or directory
- `--password`: Password for encryption or decryption

### Examples

#### Encrypt a File
```bash
python -m pycryptic.cli encrypt myfile.txt myfile.enc --password mypassword
```

#### Decrypt a File
```bash
python -m pycryptic.cli decrypt myfile.enc myfile.txt --password mypassword
```

#### Encrypt a Directory
```bash
python -m pycryptic.cli encrypt myfolder encrypted_folder --password mypassword
```

#### Decrypt a Directory
```bash
python -m pycryptic.cli decrypt encrypted_folder decrypted_folder --password mypassword
```

---

## Testing

PyCryptic includes a comprehensive test suite to ensure reliability.

1. Run all tests:
   ```bash
   pytest
   ```

2. Generate a code coverage report:
   ```bash
   pytest --cov=.
   ```

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear explanation of your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for using PyCryptic! 🔒
