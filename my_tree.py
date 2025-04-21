import os
import argparse

def print_tree(path: str, level: int = 0, max_level: int = None):
    if max_level is not None and level >= max_level:
        return

    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        print('  ' * level + '[Permission Denied]')
        return

    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = (i == len(entries) - 1)
        prefix = '└── ' if is_last else '├── '
        print('  ' * level + prefix + entry)

        if os.path.isdir(full_path):
            print_tree(full_path, level + 1, max_level)

def main():
    parser = argparse.ArgumentParser(description='Tree-like directory listing.')
    parser.add_argument('directory', nargs='?', default='.', help='Directory to list')
    parser.add_argument('-L', type=int, default=None, help='Max display depth of the directory tree')
    args = parser.parse_args()

    print(args.directory)
    print_tree(args.directory, level=0, max_level=args.L)

if __name__ == '__main__':
    main()
