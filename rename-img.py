import argparse
from pathlib import Path


def get_jpg_files():
    files_list = []
    files_list = [f for f in Path(cwd).glob('*.jpg') if f.is_file()]
    files_list.extend([f for f in Path(cwd).glob('*.JPG') if f.is_file()])
    files_list.extend([f for f in Path(cwd).glob('*.jpeg') if f.is_file()])
    files_list.extend([f for f in Path(cwd).glob('*.JPEG') if f.is_file()])
    return files_list


def get_png_files():
    files_list = []
    files_list = [f for f in Path(cwd).glob('*.png') if f.is_file()]
    files_list.extend([f for f in Path(cwd).glob('*.PNG') if f.is_file()])
    return files_list


def get_webp_files():
    files_list = []
    files_list = [f for f in Path(cwd).glob('*.webp') if f.is_file()]
    files_list.extend([f for f in Path(cwd).glob('*.WEBP') if f.is_file()])
    return files_list

def get_xcf_files():
    files_list = []
    files_list = [f for f in Path(cwd).glob('*.xcf') if f.is_file()]
    files_list.extend([f for f in Path(cwd).glob('*.XCF') if f.is_file()])
    return files_list


parser = argparse.ArgumentParser()
parser.add_argument('--prefix', '-p', type=str,
                    required=False, help='Prefix of fileame')
parser.add_argument('--count', '-c', type=int,
                    required=False, help='Count of fileame')
args = parser.parse_args()

prefix = args.prefix if args.prefix else 'IMG'
count = args.count if args.count else 1000


cwd = Path.cwd()
print(cwd)


files_list = get_jpg_files()
for filename in files_list:
    new_name = f'{prefix}-{count:05d}.jpg'
    print(f'{filename} -> {new_name}')
    filename.rename(new_name)
    count += 10

files_list = get_png_files()
for filename in files_list:
    new_name = f'{prefix}-{count:05d}.png'
    print(f'{filename} -> {new_name}')
    filename.rename(new_name)
    count += 10

files_list = get_webp_files()
for filename in files_list:
    new_name = f'{prefix}-{count:05d}.webp'
    print(f'{filename} -> {new_name}')
    filename.rename(new_name)
    count += 10

files_list = get_xcf_files()
for filename in files_list:
    new_name = f'{prefix}-{count:05d}.xcf'
    print(f'{filename} -> {new_name}')
    filename.rename(new_name)
    count += 10
