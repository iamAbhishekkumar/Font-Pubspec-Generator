import os
import argparse
from pathlib import Path


def gen(file, name):
    return f'- family: {name}\n  fonts:\n    - asset: fonts/{file}\n'


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def gen_helper_dart(name):
    var_name = name[0].lower() + name[1:]
    var_name = var_name.replace("-","")
    return f'static final {var_name} = "{name}";\n'


def main(path):
    files = os.listdir(path)
    lines = ""
    dart_lines = ""
    for file in files:
        file_name = Path(file)
        name = file_name.name.split('.')[0]
        ext = file_name.suffix
        if ext == ".ttf":
            lines += gen(file, name) + "\n"
            dart_lines += gen_helper_dart(name)

    body = f'fonts:\n{lines}'
    dart_body = f'class MyFonts {{\n {dart_lines} \n }}'

    outF = open("sample.yaml", "w")
    outF.write(body)
    outF = open("MyFont.dart", "w")
    outF.write(dart_body)
    outF.close()


parser = argparse.ArgumentParser()
parser.add_argument('--path', type=dir_path)

args = parser.parse_args()
print(f"Generating flutter pubspec for fonts present in {args.path}.....")
try:
    main(args.path)
    print("sample.yaml and MyFont.dart are generated successfully.")
except:
    print("Unexpected error occurred")
