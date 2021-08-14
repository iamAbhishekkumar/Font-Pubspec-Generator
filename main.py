import os
import argparse
from pathlib import Path


def gen(file,name):
    return f'- family: {name}\n  fonts:\n    - asset: fonts/{file}\n'

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def main(path):
    files = os.listdir(path)
    lines = ""
    for file in files: 
        file_name = Path(file)
        name = file_name.name.split('.')[0]
        ext = file_name.suffix
        if ext == ".ttf":  
            lines += gen(file,name) + "\n"

    body = f'fonts:\n{lines}'

    outF = open("sample.yaml", "w")
    outF.write(body)
    outF.close()


parser = argparse.ArgumentParser()
parser.add_argument('--path', type=dir_path)

args = parser.parse_args()
print(f"Generating flutter pubspec for fonts present in {args.path}.....")
try:
    main(args.path)
except :
    print("Unexpected error occurred")
print("sample.yaml is generated successfully")

