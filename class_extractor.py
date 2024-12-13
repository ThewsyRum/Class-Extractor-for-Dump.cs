import re

input_file = input("Enter dump path: ")
output_file = input("Enter output path: ")
class_types = input("Enter class types (e.g., 'public|private|protected'): ")

class_pattern = re.compile(
    rf'^\s*({class_types})?\s*class\s+([\w\.]+)',
    re.MULTILINE
)

class_names = []

with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

    matches = class_pattern.findall(content)
    
    for match in matches:
        class_names.append(match[1])

with open(output_file, 'w', encoding='utf-8') as file:
    for name in class_names:
        file.write(name + '\n')

print(f"Extraction completed! {len(class_names)} classes were saved in '{output_file}'.")
