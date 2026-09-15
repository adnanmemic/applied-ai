import argparse
import os
import shutil
import sys


def copy_file(src: str, dst: list[str]) -> None:
    if not src:
        raise ValueError("Error: Source cannot be empty.")

    for destination in dst:
        if not destination:
            raise ValueError("Error: Destination cannot be empty.")

        shutil.copy(src, destination)


def move_file(src: str, dst: str) -> None:
    if not src:
        raise ValueError("Error: Source cannot be empty.")

    if not dst:
        raise ValueError("Error: Destination cannot be empty.")

    shutil.move(src, dst)


def rename_file(src: str, dst: str) -> None:
    if not src:
        raise ValueError("Error: Source cannot be empty.")

    if not dst:
        raise ValueError("Error: Destination cannot be empty.")

    os.rename(src, dst)


def check_dst_len(dst: list[str]) -> bool:
    if len(dst) != 1:  # file can only be moved to one location
        print(
            "Error: argument --dst: expected exactly one argument",
            file=sys.stderr,
        )
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="file_manager",
        description="A tool that manages files. Following actions are supported: copy, move and rename",
    )
    parser.add_argument("mode", help="modes: copy, move or rename")
    parser.add_argument("--src", required=True, help="source")
    parser.add_argument("--dst", required=True, nargs="+", help="destination")
    args = parser.parse_args()

    try:
        if args.mode == "copy":
            copy_file(args.src, args.dst)
            print(f"Copied file from {args.src} to {args.dst}")

        elif args.mode == "move":
            if check_dst_len(args.dst):
                sys.exit(2)

            (destination,) = args.dst  # to avoid a list with one destination path
            move_file(args.src, destination)
            print(f"Moved file from {args.src} to {destination}")

        elif args.mode == "rename":
            if check_dst_len(args.dst):
                sys.exit(2)

            (destination,) = args.dst  # to avoid a list with one destination path
            rename_file(args.src, destination)
            print(f"Renamed {args.src} to {destination}")

        else:
            print(
                f"Error: mode must be one of: copy, mode, rename but was given '{args.mode}'",
                file=sys.stderr,
            )
            sys.exit(1)

    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    except FileNotFoundError as e:
        print(f"Error: file does not exist: {e.filename}")
        sys.exit(1)


if __name__ == "__main__":
    main()
