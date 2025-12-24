#!/usr/bin/env python3
import os
import argparse
import sys

TEXT_READ_LIMIT = 8192 

def is_text_file(path):
    try:
        with open(path, "rb") as f:
            chunk = f.read(TEXT_READ_LIMIT)
        chunk.decode("utf-8")
        return True
    except Exception:
        return False

def build_tree(root_dir, out):
    out.write("## Folder Structure\n\n")
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = "  " * level
        out.write(f"{indent}- {os.path.basename(root) or root_dir}\n")
        for f in sorted(files):
            out.write(f"{indent}  - {f}\n")
    out.write("\n---\n\n")

def dump_files(root_dir, out, max_size):
    out.write("## File Contents\n")
    for root, _, files in os.walk(root_dir):
        for file in sorted(files):
            path = os.path.join(root, file)
            relative_path = os.path.relpath(path, root_dir)

            if os.path.getsize(path) > max_size:
                continue

            if not is_text_file(path):
                continue

            out.write("\n\n---\n\n")
            out.write(f"### {relative_path}\n\n")

            try:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    out.write(f.read())
            except Exception as e:
                out.write(f"\n>Error reading file: {e}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Convert a directory of files into a single LLM-friendly context file."
    )

    parser.add_argument(
        "directory",
        help="Root directory to scan"
    )

    parser.add_argument(
        "-o", "--output",
        default="context.md",
        help="Output markdown file (default: context.md)"
    )

    parser.add_argument(
        "--max-file-size",
        type=int,
        default=300_000,
        help="Max file size in bytes (default: 300000)"
    )

    parser.add_argument(
        "--no-tree",
        action="store_true",
        help="Do not include folder structure"
    )

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Error: directory does not exist")
        sys.exit(1)

    with open(args.output, "w", encoding="utf-8") as out:
        out.write("# Project Context\n\n")

        if not args.no_tree:
            build_tree(args.directory, out)

        dump_files(args.directory, out, args.max_file_size)

    print(f"Context written to {args.output}")

if __name__ == "__main__":
    main()
