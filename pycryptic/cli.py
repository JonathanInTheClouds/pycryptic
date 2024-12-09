import os
import sys
from pycryptic.encryption import encrypt, decrypt
from pycryptic.file_utils import read_file, write_file, traverse_directory

def main():
    import argparse
    parser = argparse.ArgumentParser(description="PyCryptic - File Encryption/Decryption")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("input_path", help="File or directory to process")
    parser.add_argument("output_path", help="Output file or directory")
    parser.add_argument("--password", required=True, help="Password for encryption/decryption")

    args = parser.parse_args()

    # Validate input file/directory
    if not os.path.exists(args.input_path):
        print(f"Error: Input path '{args.input_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if os.path.isfile(args.input_path):
        data = read_file(args.input_path)
        if args.action == "encrypt":
            processed_data = encrypt(data, args.password)
        else:
            processed_data = decrypt(data, args.password)
        write_file(args.output_path, processed_data)

    elif os.path.isdir(args.input_path):
        for file_path in traverse_directory(args.input_path):
            relative_path = os.path.relpath(file_path, args.input_path)
            output_file_path = os.path.join(args.output_path, relative_path)
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            data = read_file(file_path)
            if args.action == "encrypt":
                processed_data = encrypt(data, args.password)
            else:
                processed_data = decrypt(data, args.password)
            write_file(output_file_path, processed_data)

if __name__ == "__main__":
    main()
