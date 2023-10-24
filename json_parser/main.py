import sys
from parser_validation import is_valid_json


def main(file_path):
    json_string = read_json_file(file_path)

    if is_valid_json(json_string):
        print("Valid JSON")
        return True
    else:
        print("Invalid JSON")
        return False


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    main("tests/step4/valid.json")
