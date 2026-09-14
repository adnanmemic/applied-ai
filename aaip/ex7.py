import argparse
import sys


def copy_file(src: str, dst: list[str]) -> None:
    pass


def move_file(src: str, dst: str) -> None:
    pass


def rename_file(src: str, dst: str) -> None:
    pass


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="file_manager",
        description="A tool that manages file. Following actions are supported: copy, move and rename",
    )
    parser.add_argument("mode", help="modes: copy, move or rename")
    parser.add_argument("--src", required=True, help="source")
    parser.add_argument("--dst", required=True, nargs="+", help="destination")
    args = parser.parse_args()
    print(args)

    if args.mode == "copy":
        copy_file(args.src, args.dst)
        print(f"Copied file from {args.src} to {args.dst}")
    elif args.mode == "move":
        if len(args.dst) != 1:  # file can only be moved to one location
            print(
                "Error: argument --dst: expected exactly one argument", file=sys.stderr
            )
            sys.exit(2)
        (destination,) = args.dst  # to avoid a list with one destination path
        move_file(args.src, args.dst)
        print(f"Moved file from {args.src} to {destination}")
    elif args.mode == "rename":
        if len(args.dst) != 1:  # file can only be renamed to one name
            print(
                "Error: argument --dst: expected exactly one argument", file=sys.stderr
            )
            sys.exit(2)
        (destination,) = args.dst  # to avoid a list with one destination path
        rename_file(args.src, args.dst)
        print(f"Renamed file to {destination}")
    else:
        print(
            f"Error: mode must be one of: copy, mode, rename but was given '{args.mode}'",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
