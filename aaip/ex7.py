import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="file_manager",
        description="A tool that manages file. Following actions are supported: copy, move and rename",
    )
    parser.add_argument("mode", help="modes: copy, move or rename")
    parser.add_argument("--src", help="source")
    parser.add_argument("--dst", help="destination")
    args = parser.parse_args()
    print(args)

    if args.mode == "copy":
        print(f"Copied file from {args.src} to {args.dst}")
    elif args.mode == "move":
        print(f"Moved file from {args.src} to {args.dst}")
    elif args.mode == "rename":
        print(f"Renamed file to {args.dst}")


if __name__ == "__main__":
    main()
