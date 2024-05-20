import sys


def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file


if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    print(f"Input File: {input_file}")
    print(f"Output File: {output_file}")

import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Opcjonalnie: Weryfikacja składni za pomocą schematu JSON
            return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
        print(f"Data: {data}")
    else:
        print("Unsupported input format")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving JSON file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    else:
        print("Unsupported output format")
        sys.exit(1)

import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        print(f"Invalid YAML format: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
    except Exception as e:
        print(f"Error saving YAML file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        save_yaml(data, output_file)
    else:
        print("Unsupported output format")
        sys.exit(1)

import xml.etree.ElementTree as ET

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Invalid XML format: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)

def save_xml(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path)
    except Exception as e:
        print(f"Error saving XML file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
    else:
        print("Unsupported input format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    else:
        print("Unsupported output format")
        sys.exit(1)

