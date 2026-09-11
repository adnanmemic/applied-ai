import sys


def count_words(path: str) -> int:
    pass


def count_lines(path: str) -> int:
    pass


def search_word(path: str, word: str) -> list[str]:
    pass

def main() -> None:
    args = len(sys.argv) - 1  # ignore the filename
    if args < 2:
        print("error: expected at least 2 arguments", file=sys.stderr)
        sys.exit(2)

    file_path = sys.argv[1]
    action = sys.argv[2]

    if action == "count_words":
        count_words(file_path)
    elif action == "count_lines":
        count_lines(file_path)
    elif action == "search_word":
        if args < 3:
            print("error: expected at least 3 arguments", file=sys.stderr)
            sys.exit(2)

        word = sys.argv[3] 
        search_word(file_path, word)
    else:
        print(
            "error: action must be one of: ",
            "\n - count_words",
            "\n - count_lines",
            "\n - search_word",
            file=sys.stderr,
        )
        sys.exit(2)

if __name__ == "__main__":
    main()
