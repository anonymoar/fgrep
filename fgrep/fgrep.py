import argparse
import re
import sys
from contextlib import ExitStack, nullcontext
from typing import List


def fgrep(template: str, file_names: List[str], ignore_case: bool = False):
    file_names = set(file_names)
    ctx_manager = ExitStack() if file_names else nullcontext()
    result_template = "{file_name}: {line}" if len(file_names) > 1 else "{line}"

    if ignore_case:

        def find_pattern(pattern: str, line: str):
            return re.search(pattern, line, re.IGNORECASE)

    else:

        def find_pattern(pattern: str, line: str):
            return pattern in line

    with ctx_manager:
        if file_names:
            sources = [ctx_manager.enter_context(open(file_name)) for file_name in file_names]
        else:
            sources = [sys.stdin]

        matches = []
        for f in sources:
            for line in f:
                if find_pattern(template, line):
                    matches.append(result_template.format(file_name=f.name, line=line.strip()))

        return "\n".join(matches)


def main():
    parser = argparse.ArgumentParser(description="fgrep command")
    parser.add_argument("template", help="search template")
    parser.add_argument("file_names", nargs="*", help="search sources")
    parser.add_argument("-i", "--ignore_case", action="store_true")
    args = parser.parse_args()

    try:
        result = fgrep(args.template, args.file_names, args.ignore_case)

        if not result:
            exit(1)

        print(result)
    except FileNotFoundError as e:
        print(f"{e.filename}: {e.strerror}", file=sys.stderr)
        exit(2)


if __name__ == "__main__":
    main()
